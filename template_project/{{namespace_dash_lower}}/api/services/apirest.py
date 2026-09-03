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

from api.services.configuration import configuration
from api.libraries.autoload import import_all
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, Optional, Dict
from fastapi import FastAPI

# Objet contenant le serveur de l'API REST.
apirest: Optional[FastAPI] = None

if not apirest:
  arconf: Dict[str, Any] = configuration["apirest"]
  
  # Définition du serveur.
  apirest: FastAPI = FastAPI(
    title=arconf["title"],
    description=arconf["description"],
    version=arconf["version"])
  
  # Autorisations des middlewares.
  apirest.add_middleware(CORSMiddleware,
    allow_credentials=arconf["credentials"],
    allow_origins=arconf["origins"], 
    allow_methods=arconf["methods"], 
    allow_headers=arconf["headers"])

  # Chargement des routes.
  prefix: str = f"/api/{arconf["version"]}"
  for router in import_all("api/routes", "router"):
    apirest.include_router(router, prefix=prefix)