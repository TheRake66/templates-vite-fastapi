"""
Nom du module         : main.py
Description           : Point d'entrée de l'application.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from api.services.configuration import configuration
from api.services.application import application
from api.services.websocket import websocket
from api.services.apirest import apirest
from typing import Any, Dict
from uvicorn import run

# Lancement de l'application.
svconf: Dict[str, Any] = configuration["server"]
run(application, 
  host=svconf["address"], 
  port=svconf["port"],
  reload=svconf["reload"],
  access_log=svconf["debug"])

# Route racine de l'API REST.
@apirest.get("/")
async def root() -> None:
  pass

# Gestion de la connexion aux WebSockets.
@websocket.event
async def connect(sid: str, environ: Dict[str, Any]) -> None:
  pass

# Gestion de la déconnexion aux WebSockets.
@websocket.event
async def disconnect(sid: str) -> None:
  pass