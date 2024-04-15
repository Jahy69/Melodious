from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import re
import logging

from config import ApplicationConfig
from logging_config import setup_logging
from initialization import initialize_app
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  # Regrouped imports
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS

app = Flask(__name__)
CORS(app)
load_dotenv()
setup_logging()

# Environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# File paths
script_dir = os.path.dirname(__file__)
csv_folder = os.path.join(script_dir, "CSV")
csv_descriptions_path = os.path.join(csv_folder, "genres_musicaux_descriptions.csv")
csv_names_path = os.path.join(csv_folder, "genres_musicaux_names.csv")

# Application initialization
if not initialize_app(csv_descriptions_path, csv_names_path):
    logging.error("Failed to initialize the application.")
    exit(1)  # Exit if initialization fails

# Data loading using CSVLoader
loader = CSVLoader(
    file_path=csv_descriptions_path, encoding="utf-8", csv_args={"delimiter": ","}
)
data = loader.load()

# Embeddings and vector store initialization
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
logging.info("Embeddings created.")
vectorstore = FAISS.from_documents(data, embeddings)
logging.info("Vectorstore created successfully.")


# Fonction pour obtenir un token Spotify en utilisant l'ID client et le secret client
def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"  # URL de l'API Spotify pour obtenir un token
    response = requests.post(
        url, data={"grant_type": "client_credentials"}, auth=(client_id, client_secret)
    )  # Envoie une requête POST pour obtenir un token
    if response.status_code == 200:  # Si la requête réussit
        return response.json()["access_token"]  # Retourne le token d'accès
    else:
        raise Exception(
            "Failed to retrieve token"
        )  # Lève une exception si la requête échoue


# Fonction pour chercher les playlists Spotify en se basant sur le genre detecté
def find_spotify_playlists_by_genre(access_token, genre):
    url = "https://api.spotify.com/v1/search"  # Définit l'URL de l'API de recherche Spotify
    headers = {
        "Authorization": f"Bearer {access_token}"
    }  # Prépare les en-têtes avec le token d'accès pour l'autorisation
    params = {
        "q": f"{genre}",
        "type": "playlist",
        "limit": 10,
    }  # Paramètres de la requête pour chercher des playlists correspondant au genre spécifié avec une limite de 10 résultats
    response = requests.get(
        url, headers=headers, params=params
    )  # Effectue la requête GET à l'API Spotify avec les paramètres et en-têtes définis
    if response.status_code == 200:  # Vérifie si la requête a réussi
        playlists = response.json()["playlists"][
            "items"
        ]  # Extrait les playlists de la réponse JSON
        filtered_playlists = [
            playlist
            for playlist in playlists
            if genre.lower() in playlist["name"].lower()
        ]  # Filtre les playlists pour inclure uniquement celles dont le nom contient le genre recherché
        limited_playlists = filtered_playlists[
            :3
        ]  # Limite le nombre de playlists renvoyées à 3 pour simplifier la réponse
        return [
            {"name": playlist["name"], "url": playlist["external_urls"]["spotify"]}
            for playlist in limited_playlists
        ]  # Retourne une liste de dictionnaires avec le nom et l'URL de chaque playlist sélectionnée
    else:
        raise Exception(
            "Failed to search playlists"
        )  # Lève une exception si la recherche échoue


# Définit une fonction pour filtrer la réponse basée sur la présence de mots-clés liés à la musique
def filter_response_for_music_theme(response):
    music_keywords = [
        "musique",
        "chanson",
        "instrument",
        "note",
        "mélodie",
        "concert",
        "harmonie",
        "rythme",
        "genre musical",
        "clip",
        "BPM",
        "artiste",
        "orchestre",
        "symphonie",
        "opéra",
        "solo",
        "accord",
        "partition",
        "compositeur",
        "interprète",
        "production musicale",
        "studio d'enregistrement",
        "mixage",
        "mastering",
        "sample",
        "beat",
        "riff",
        "guitare",
        "piano",
        "batterie",
        "basse",
        "synthétiseur",
        "DJ",
        "performance live",
        "festival de musique",
        "critique musicale",
        "échelle musicale",
        "tempo",
        "clef musicale",
        "signature rythmique",
        "improvisation",
        "technique vocale",
        "chorale",
        "bande originale",
        "score",
        "histoire",
        "soundtrack",
        "licence musicale",
        "droits d'auteur musicaux",
        "distribution musicale",
        "promotion musicale",
        "playlist",
        "streaming musical",
        "téléchargement de musique",
        "vinyle",
        "CD",
        "cassette audio",
        "radio",
        "mélomane",
        "auditeur",
        "fan de musique",
        "concert en direct",
        "tournée",
        "billetterie musicale",
        "merchandising musical",
        "biographie d'artiste",
        "histoire de la musique",
        "théorie musicale",
        "acoustique",
        "éducation musicale",
        "critère de succès musical",
        "récompenses musicales",
        "Grammy",
        "Billboard",
        "charts musicaux",
        "MTV Music Awards",
    ]  # Liste des mots-clés associés à la musique
    return any(
        keyword in response.lower() for keyword in music_keywords
    )  # Vérifie si au moins un mot-clé est présent dans la réponse


# Définit une fonction pour détecter le genre musical dans la requête de l'utilisateur
def detect_genre_in_query(query, genre_names):
    """Détecte si un genre musical se trouve dans la requête."""
    query = query.lower()
    for genre in genre_names:
        genre_pattern = r"\b" + re.escape(genre.lower()) + r"\b"
        if re.search(genre_pattern, query):
            return genre
    return None


def nettoyer_texte(texte):
    # Remplacer les séquences de deux sauts de ligne consécutifs par un seul
    texte_avec_un_seul_n = re.sub(r"\n\n", "\n", texte)
    # Remplacer les sauts de ligne isolés par des espaces
    texte_sans_n_isoles = texte_avec_un_seul_n.replace("\n", " ")
    # Supprimer les marqueurs de lien
    texte_sans_liens = re.sub(r"\[Lien\]", "", texte_sans_n_isoles)

    return texte_sans_liens


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # Récupère les données JSON envoyées par l'utilisateur
    query = data.get(
        "query"
    )  # Extrait la requête de l'utilisateur à partir des données
    if (
        not openai_api_key or not vectorstore
    ):  # Vérifie si la clé API OpenAI ou le vectorstore est configuré
        return (
            jsonify({"error": "API key or vectorstore not configured."}),
            400,
        )  # Retourne un message d'erreur si la configuration est manquante

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(
            temperature=0.0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key
        ),
        retriever=vectorstore.as_retriever(),
    )  # Crée une chaîne de récupération conversationnelle avec les paramètres spécifiés pour OpenAI

    history = []  # Initialise l'historique de la conversation

    result = chain(
        {"question": query, "chat_history": history}
    )  # Utilise la chaîne pour générer une réponse basée sur la requête et l'historique
    history.append(
        (query, result["answer"])
    )  # Ajoute la requête et la réponse à l'historique

    genre_detected = detect_genre_in_query(
        query
    )  # Détecte un genre musical dans la requête de l'utilisateur
    # Vérifie si la réponse inclut des mots-clés musicaux ou si un genre a été détecté
    if filter_response_for_music_theme(result["answer"]) or genre_detected:
        # Prépare la structure de réponse incluant la réponse et une liste de playlists
        response = {"answer": result["answer"], "playlists": []}
        if genre_detected:  # Si un genre musical est détecté
            try:
                # Obtient un token d'accès Spotify à l'aide des identifiants client
                access_token = get_spotify_token(
                    spotify_client_id, spotify_client_secret
                )
                # Recherche des playlists Spotify correspondant au genre détecté
                playlists = find_spotify_playlists_by_genre(
                    access_token, genre_detected
                )
                if playlists:  # Si des playlists sont trouvées
                    playlist_texts = (
                        []
                    )  # Initialise une liste pour stocker les textes des playlists
                    for playlist in playlists:
                        # Ajoute le nom et l'URL de chaque playlist trouvée à la liste
                        playlist_texts.append(f"{playlist['name']}: {playlist['url']}")
                    response["playlists"] = (
                        playlists  # Met à jour la réponse avec les playlists trouvées
                    )
            except Exception as e:
                # Gère les exceptions et imprime l'erreur si la recherche de playlists échoue
                print(f"Erreur lors de la recherche de playlists Spotify: {e}")
        # Nettoie le texte de la réponse avant de le retourner
        response["answer"] = nettoyer_texte(response["answer"])
        return jsonify(response)  # Retourne la réponse au format JSON
    else:
        # Retourne une réponse indiquant que la requête n'est pas suffisamment liée à la musique
        return jsonify(
            {
                "answer": "La réponse n'est pas suffisamment liée au thème musical. Veuillez essayer avec une question différente."
            }
        )


# Point d'entrée principal pour exécuter l'application Flask en mode debug
if __name__ == "__main__":
    if initialize_app(
        csv_descriptions_path, csv_names_path
    ):  # Initialise l'application avec le chemin vers le CSV
        app.run(
            debug=True
        )  # Démarre l'application Flask seulement si l'initialisation est réussie
    else:
        print("Failed to initialize the application.")
