from config import (
    ApplicationConfig,
)  # Import the ApplicationConfig class from the config module
import logging  # Import the logging module for logging information and errors
from logging_config import (
    setup_logging,
)  # Import the setup_logging function from the logging_config module


def initialize_app(descriptions_path, names_path):
    """
    Initialize the application with the given descriptions and names paths.

    This function initializes the application by creating an instance of the ApplicationConfig class with the provided
    descriptions and names paths. It then attempts to load genres from a CSV file using the load_genres_from_csv()
    method. If the genres are loaded successfully, the function logs an informational message and returns True.
    Otherwise, the function logs an error message and returns False.

    Args:
    descriptions_path (str): The path to the descriptions CSV file.
    names_path (str): The path to the names CSV file.

    Returns:
    bool: True if the application is initialized successfully, False otherwise.
    """
    config = ApplicationConfig(
        descriptions_path, names_path
    )  # Create an instance of the ApplicationConfig class

    if config.load_genres_from_csv():  # Attempt to load genres from a CSV file
        logging.info(
            "Application initialized successfully."
        )  # Log an informational message
        return True
    else:
        logging.error("Application initialization failed.")  # Log an error message
        return False
