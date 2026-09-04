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

from services.configuration import configuration, Json
from services.application import application
from services.websocket import websocket
from services.apirest import apirest
from typing import Any, Dict
from uvicorn import run

# Lancement de l'application.
if __name__ == "__main__":
  apconf: Json = configuration["server"]
  run("main:application", 
    host=apconf["address"], 
    port=apconf["port"],
    reload=apconf["reload"],
    access_log=apconf["debug"])

# Route racine de l'API REST.
@apirest.get("/")
async def root() -> None:
  pass

# Gestion de la connexion aux WebSockets.
@websocket.event
async def connect(sid: str) -> None:
  pass

# Gestion de la déconnexion aux WebSockets.
@websocket.event
async def disconnect(sid: str) -> None:
  pass