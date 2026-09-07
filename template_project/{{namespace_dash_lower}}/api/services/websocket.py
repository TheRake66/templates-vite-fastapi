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
from libraries.response import Response
from socketio import AsyncServer
from typing import Optional

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

def user_connected() -> int:
  """Ajoute un utilisateur à la liste pour le compteurs.

  Returns:
    int: Le nombre d'utilisateurs connectés.
  """
  global __count
  __count += 1
  return __count

def user_disconnected() -> int:
  """Retire un utilisateur de la liste pour le compteurs.

  Returns:
    int: Le nombre d'utilisateurs connectés.
  """
  global __count
  __count -= 1
  return __count

async def emit_data(event: str, data: Response, 
  room: Optional[str] = None, sid: Optional[str] = None) -> None:
  """Envoi des données depuis le serveur.

  Arguments:
    event (str): Le nom de l'événement.
    data (Response): Les données à envoyer.
    room (Optional[str]): Le nom du salon dans lequel envoyer les données. Aucun par défaut.
    sid (Optional[str]): L'identifiant du WebSocket à qui envoyer les données. Aucun par défaut.
  """
  await websocket.emit(event, data.model_dump(), room=room, to=sid)

# Nombre d'utilisateurs connectés.
__count: int = 0

# Objet contenant le serveur de l'API REST.
websocket: AsyncServer = __init_asyncserver()