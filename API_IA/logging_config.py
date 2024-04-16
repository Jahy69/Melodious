import logging
from logging import Formatter

# Function to set up logging configuration
def setup_logging():
    # Set level of logger to INFO
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Create a custom logger
    logger = logging.getLogger(__name__)
    
    # Create a formatter for log messages
    formatter = Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create a file handler for the logger
    file_handler = logging.FileHandler("chatbot.log")

    # Set the formatter for the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Create a console handler for the logger
    console_handler = logging.StreamHandler()

    # Set the formatter for the console handler
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

# Call the setup_logging function to configure logging
setup_logging()

# Define the logger object
logger = logging.getLogger(__name__)