import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["monitor_internet"]

logs_collection = db["webpages"]

# Crear índices
logs_collection.create_index("usuario")
logs_collection.create_index("dominio")
logs_collection.create_index("fecha_servidor")