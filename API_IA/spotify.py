import requests
import logging
from logging_config import setup_logging, logger


# Function to obtain a Spotify token using the client ID and client secret
def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"  # Spotify API URL to obtain a token
    response = requests.post(
        url, data={"grant_type": "client_credentials"}, auth=(client_id, client_secret)
    )  # Sends a POST request to obtain a token
    if response.status_code == 200:  # If the request is successful
        logger.info("Successfully retrieved Spotify token")
        return response.json()["access_token"]  # Returns the access token
    else:
        logger.error("Failed to retrieve Spotify token")
        raise Exception(
            "Failed to retrieve token"
        )  # Raises an exception if the request fails


# Function to find Spotify playlists based on the detected genre
def find_spotify_playlists_by_genre(access_token, genre):
    url = "https://api.spotify.com/v1/search"  # Defines the Spotify search API URL
    headers = {
        "Authorization": f"Bearer {access_token}"
    }  # Prepares the headers with the access token for authorization
    params = {
        "q": f"{genre}",
        "type": "playlist",
        "limit": 10,
    }  # Request parameters to search for playlists matching the specified genre with a limit of 10 results
    response = requests.get(
        url, headers=headers, params=params
    )  # Performs the GET request to the Spotify API with the defined parameters and headers
    if response.status_code == 200:  # Checks if the request was successful
        logger.info("Successfully searched Spotify playlists")
        playlists = response.json()["playlists"][
            "items"
        ]  # Extracts the playlists from the JSON response
        filtered_playlists = [
            playlist
            for playlist in playlists
            if genre.lower() in playlist["name"].lower()
        ]  # Filters the playlists to include only those whose name contains the searched genre
        limited_playlists = filtered_playlists[
            :3
        ]  # Limits the number of playlists returned to 3 for simplicity
        return [
            {"name": playlist["name"], "url": playlist["external_urls"]["spotify"]}
            for playlist in limited_playlists
        ]  # Returns a list of dictionaries with the name and URL of each selected playlist
    else:
        logger.error("Failed to search Spotify playlists")
        raise Exception(
            "Failed to search playlists"
        )  # Raises an exception if the search fails
