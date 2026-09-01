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

def __add_routers(*routers: APIRouter) -> None:
  """Enregistre un ensemble de routeurs en ajoutant un préfixe global.

  Arguments:
    *routers: Les routeurs à ajouter à l'application.
  """
  prefix = f"/api/{configuration["version"]}"
  for router in routers:
    application.include_router(router, prefix=prefix)