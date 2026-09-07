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

from services.websocket import websocket, \
  user_connected, user_disconnected
from services.application import application
from services.apirest import apirest
from libraries.configuration import configuration, Json
from libraries.response import Response
from libraries.broadcast import BroadCast
from libraries.multicast import MultiCast
from libraries.unicast import UniCast
from typing import Dict, Any
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
  return Response(message="Hello World!")

# Gestion de la connexion aux WebSockets.
@websocket.event
async def connect(sid: str, environ: Dict[str, Any]) -> None:
  if user_connected() == 1:
    BroadCast.start_all()

# Gestion de la déconnexion aux WebSockets.
@websocket.event
async def disconnect(sid: str) -> None:
  UniCast.cleanup_sid(sid)
  MultiCast.cleanup_sid(sid)
  if user_disconnected() == 0:
    BroadCast.stop_all()