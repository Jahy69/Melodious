import logging
import csv


class ApplicationConfig:
    def __init__(self, csv_descriptions_path, csv_names_path):
        """
        Initialize the ApplicationConfig class with the paths to the CSV files containing genre descriptions and names.
        """
        self.csv_descriptions_path = csv_descriptions_path
        self.csv_names_path = csv_names_path
        self.known_genres = None
        self.genre_names = None

    def load_genres_from_csv(self):
        """
        Load genres from the CSV files and store them in the class attributes.
        Return True if successful, False otherwise.
        """
        try:
            with open(self.csv_descriptions_path, "r") as file:
                self.known_genres = list(csv.reader(file))
            with open(self.csv_names_path, "r") as file:
                self.genre_names = [row[0] for row in csv.reader(file)]
            logging.info("Genres loaded successfully.")
            return True
        except Exception as e:
            logging.error(f"Failed to load genres: {str(e)}")
            return False
