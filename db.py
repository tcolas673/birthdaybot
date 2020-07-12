import os
import urllib.parse
from pymongo import MongoClient

# from dotenv import load_dotenv
# load_dotenv()

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
URL = os.getenv("URL")

def connect():
    password = urllib.parse.quote_plus(DATABASE_PASSWORD)

    client = MongoClient(URL % (password))
    db = client.get_database('birthdays_db')
    
    birthdays = db.birthday1

    return birthdays