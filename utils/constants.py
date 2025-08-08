from dotenv import load_dotenv
import os

# .env-Datei laden
load_dotenv()

# Konstanten abrufen
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL")
BASE_URL_store = os.getenv("BASE_URL_shop")

