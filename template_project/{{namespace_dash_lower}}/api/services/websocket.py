"""
Nom du module         : websocket.py
Description           : Module gérant le serveur des WebSockets.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from services.configuration import configuration, Json
from typing import Any, Optional, Dict
from socketio import AsyncServer

# Objet contenant le serveur de l'API REST.
websocket: Optional[AsyncServer] = None

if not websocket:
  wsconf: Json = configuration["websocket"]
  
  # Définition du serveur.
  websocket = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=wsconf["origins"],
    logger=wsconf["debug"],
    engineio_logger=wsconf["debug"])