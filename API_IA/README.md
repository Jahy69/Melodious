
# Music recommendation AI
This project is an API built with Flask and integrating LanguageChain and OpenAI, specially designed to offer music-related functionalities. It can process text queries and provide music-related answers thanks to artificial intelligence.

## Initial configuration
Before launching the API, a few configuration steps are required.

### Prerequisites
- Python 3.8 or later.
- pip (Python package manager).
- Python virtual environment (recommended).

## Installation

Clone the Github :
```bash
git clone <url_of_repository>
cd <project_folder_name>
```
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
    
## Environment Variables

Open the .env file and modify the values of the environment variables to match your configuration

`OPENAI_API_KEY` = Your OpenAI API key.

`SPOTIFY_CLIENT_ID` = Your Spotify application ID.

`SPOTIFY_CLIENT_SECRET` = Your Spotify application secret client.

Don't forget to rename the env_example file to .env

## Start
To start the API, use the following command in the project root directory:
``bash
  python3 API.py
```

This will launch the Flask API on localhost with the default port 5000. You can access the API via http://localhost:5000.
