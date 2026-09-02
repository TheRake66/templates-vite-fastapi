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

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from api.utils.configuration import configuration
from api.utils.autoload import import_all
from pathlib import Path

# Définition de l'application.
application = FastAPI(
  title=configuration["title"],
  description=configuration["description"],
  version=configuration["version"])

# Autorisations des middlewares.
application.add_middleware(CORSMiddleware,
  allow_credentials=configuration["credentials"],
  allow_origins=configuration["origins"], 
  allow_methods=configuration["methods"], 
  allow_headers=configuration["headers"])

# Charge toutes les routes.
prefix: str = f"/api/{configuration["version"]}"
routes: Path = Path("api/routes")
routers: APIRouter = import_all(routes, "router")
for router in routers:
  application.include_router(router, prefix=prefix)