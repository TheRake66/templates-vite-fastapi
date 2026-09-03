"""
Nom du module         : main.py
Description           : Point d'entrée du serveur FastAPI.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from api.utils.configuration import config
from api.utils.autoload import import_all
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# Définition de l'application.
application = FastAPI(
  title=config["title"],
  description=config["description"],
  version=config["version"])

# Autorisations des middlewares.
application.add_middleware(CORSMiddleware,
  allow_credentials=config["credentials"],
  allow_origins=config["origins"], 
  allow_methods=config["methods"], 
  allow_headers=config["headers"])

# Charge toutes les routes.
prefix: str = f"/api/{config["version"]}"
for router in import_all("api/routes", "router"):
  application.include_router(router, prefix=prefix)