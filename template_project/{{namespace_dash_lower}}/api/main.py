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

from libraries.configuration import configuration, Json
from services.application import application
from services.websocket import websocket
from services.apirest import apirest
from libraries.unicast import UniCast
from uvicorn import run

# Lancement de l'application.
if __name__ == "__main__":
  config: Json = configuration["server"]
  run("main:application", 
    host=config["address"], 
    port=config["port"],
    reload=config["reload"],
    access_log=config["debug"])

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
  UniCast.cleanup_sid(sid)