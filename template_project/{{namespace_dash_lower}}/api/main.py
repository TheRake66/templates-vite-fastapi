"""
Nom du module         : main.py
Description           : Point d'entrée de l'application.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
  L'import inutilisé "application" est nécessaire, c'est cette variable
  que Uvicorn utilise pour lancer le serveur.
"""

from services.application import application
from services.websocket import websocket, \
  user_connected, user_disconnected
from services.apirest import apirest
from libraries.response import Response
from libraries.broadcast import BroadCast
from libraries.multicast import MultiCast
from libraries.unicast import UniCast
from typing import Dict, Any

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