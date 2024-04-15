from config import ApplicationConfig
import logging


def initialize_app(descriptions_path, names_path):
    config = ApplicationConfig(descriptions_path, names_path)
    if config.load_genres_from_csv():
        logging.info("Application initialized successfully.")
        return True
    else:
        logging.error("Application initialization failed.")
        return False
