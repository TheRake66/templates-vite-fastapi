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

from services.repository import get_remote, manager
from libraries.configuration import configuration, Json
from libraries.response import Response
from socketio import AsyncServer, AsyncRedisManager
from redis.asyncio import Redis
from typing import Optional

def __init_asyncserver() -> AsyncServer:
  """Initialise le service AsyncServer.

  Returns:
    AsyncServer: Le service AsyncServer.
  """
  # Chargement de la configuration.
  config: Json = configuration["websocket"]
  
  # Définition du manager Redis.
  client: Optional[AsyncRedisManager] = None
  if isinstance(manager, Redis):
    client = AsyncRedisManager(get_remote())
  
  # Définition du serveur.
  websocket: AsyncServer = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=config["origins"],
    engineio_logger=config["debug"],
    logger=config["debug"],
    client_manager=client)
  
  # On retourne le service.
  return websocket

def user_connected() -> int:
  """Incrémente le compteur du nombre d'utilisateurs.

  Returns:
    int: Le nombre d'utilisateurs connectés.
  """
  global __count
  __count += 1
  return __count

def user_disconnected() -> int:
  """Décrémente le compteur du nombre d'utilisateurs.

  Returns:
    int: Le nombre d'utilisateurs connectés.
  """
  global __count
  __count -= 1
  return __count

async def emit_data(event: str, data: Response, sid: Optional[str] = None) -> None:
  """Envoi des données depuis le serveur.

  Arguments:
    event (str): Le nom de l'événement.
    data (Response): Les données à envoyer.
    sid (Optional[str]): L'identifiant du WebSocket cible. Aucun par défaut.
  """
  await websocket.emit(event, data.model_dump(), to=sid)

__count: int = 0
"""Nombre d'utilisateurs connectés."""

websocket: AsyncServer = __init_asyncserver()
"""Objet contenant le serveur de l'API REST."""