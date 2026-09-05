"""
Nom du module         : apirest.py
Description           : Module gérant le serveur de l'API REST.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from services.configuration import configuration, Json
from libraries.autoload import import_all
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from typing import Optional

# Objet contenant le serveur de l'API REST.
apirest: Optional[FastAPI] = None

if not apirest:
  config: Json = configuration["apirest"]
  
  # Définition du serveur.
  apirest: FastAPI = FastAPI(
    title=config["title"],
    description=config["description"],
    version=config["version"])
  
  # Autorisations des middlewares.
  apirest.add_middleware(CORSMiddleware,
    allow_credentials=config["credentials"],
    allow_origins=config["origins"], 
    allow_methods=config["methods"], 
    allow_headers=config["headers"])

  # Chargement des routes.
  prefix: str = f"/api/{config["version"]}"
  for router in import_all("routes", "router"):
    apirest.include_router(router, prefix=prefix)