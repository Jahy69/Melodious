import logging
from logging_config import setup_logging, logger


def filter_response_for_music_theme(response):
    """
    This function checks if a given response contains any music-related keywords.
    It returns True if at least one keyword is found, and False otherwise.
    """
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
    ]  # List of music-related keywords

    logger.debug(f"Checking response for music keywords: {response}")

    return any(
        keyword in response.lower() for keyword in music_keywords
    )  # Checks if at least one keyword is present in the response
