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

from libraries.configuration import configuration, Json
from socketio import AsyncServer

def __init_asyncserver() -> AsyncServer:
  """Initialise le service AsyncServer.

  Returns:
    AsyncServer: Le service AsyncServer.
  """
  # Chargement de la configuration.
  config: Json = configuration["websocket"]
  
  # Définition du serveur.
  websocket: AsyncServer = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=config["origins"],
    engineio_logger=config["debug"],
    logger=config["debug"])
  
  # On retourne le service.
  return websocket

# Objet contenant le serveur de l'API REST.
websocket: AsyncServer = __init_asyncserver()