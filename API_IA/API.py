from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import re
import logging

from config import ApplicationConfig
from logging_config import setup_logging, logger
from initialization import initialize_app
from filter_response import filter_response_for_music_theme
from spotify import get_spotify_token, find_spotify_playlists_by_genre
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS

app = Flask(__name__)
CORS(app)
#load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

script_dir = os.path.dirname(__file__)
csv_folder = os.path.join(script_dir, "CSV")

csv_descriptions_path = os.path.join(csv_folder, "genres_musicaux_descriptions.csv")
csv_names_path = os.path.join(csv_folder, "genres_musicaux_names.csv")

app_config = ApplicationConfig(csv_descriptions_path, csv_names_path)

if not app_config.load_genres_from_csv():
    logging.error("Failed to load genres.")
    exit(1)

if not initialize_app(csv_descriptions_path, csv_names_path):
    logging.error("Failed to initialize the application.")
    exit(1)

loader = CSVLoader(
    file_path=csv_descriptions_path, encoding="utf-8", csv_args={"delimiter": ","}
)
data = loader.load()

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
logging.info("Embeddings created.")

vectorstore = FAISS.from_documents(data, embeddings)
logging.info("Vectorstore created successfully.")

def detect_genre_in_query(query, genre_names):
    query = query.lower()
    logging.debug(f"Query: {query}")
    for genre in genre_names:
        if isinstance(genre, list):
            genre = genre[0]
        genre_pattern = r"\b" + re.escape(genre.lower()) + r"\b"
        if re.search(genre_pattern, query):
            logging.info(f"Detected genre: {genre}")
            return genre
    logging.info("No genre detected")
    return None


def nettoyer_texte(texte):
    texte_avec_un_seul_n = re.sub(r"\n\n", "\n", texte)
    texte_sans_n_isoles = texte_avec_un_seul_n.replace("\n", " ")
    texte_sans_liens = re.sub(r"\[Lien\]", "", texte_sans_n_isoles)

    return texte_sans_liens


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query")
    if not openai_api_key or not vectorstore:
        return (
            jsonify({"error": "API key or vectorstore not configured."}),
            400,
        )

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(
            temperature=0.0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key
        ),
        retriever=vectorstore.as_retriever(),
    )

    history = []

    # Add logging here
    logger.info("Processing query: %s", query)

    result = chain({"question": query, "chat_history": history})
    history.append((query, result["answer"]))

    genre_detected = detect_genre_in_query(query, app_config.genre_names)

    if filter_response_for_music_theme(result["answer"]) or genre_detected:
        response = {"answer": result["answer"], "playlists": []}
        if genre_detected:
            try:
                access_token = get_spotify_token(
                    spotify_client_id, spotify_client_secret
                )
                playlists = find_spotify_playlists_by_genre(
                    access_token, genre_detected
                )
                if playlists:
                    playlist_texts = []
                    for playlist in playlists:
                        playlist_texts.append(f"{playlist['name']}: {playlist['url']}")
                    response["playlists"] = playlists
            except Exception as e:
                logger.error("Error while searching Spotify playlists: %s", e)
                print(f"Erreur lors de la recherche de playlists Spotify: {e}")
        response["answer"] = nettoyer_texte(response["answer"])
        return jsonify(response)
    else:
        return jsonify(
            {
                "answer": "La réponse n'est pas suffisamment liée au thème musical. Veuillez essayer avec une question différente."
            }
        )

if __name__ == "__main__":
    if initialize_app(csv_descriptions_path, csv_names_path):
        app.run(
            debug=True
        )
    else:
        print("Failed to initialize the application.")
