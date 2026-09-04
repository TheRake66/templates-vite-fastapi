"""
Nom du module         : application.py
Description           : Module gérant l'application principale.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from services.configuration import configuration, Json
from services.websocket import websocket
from services.apirest import apirest
from typing import Any, Optional, Dict
from socketio import ASGIApp

# Objet contenant le serveur de l'application.
application: Optional[ASGIApp] = None

if not application:
  wsconf: Json = configuration["websocket"]
  
  # Définition du serveur.
  application: ASGIApp = ASGIApp(
    socketio_server=websocket,
    other_asgi_app=apirest,
    socketio_path=wsconf["urlpath"])