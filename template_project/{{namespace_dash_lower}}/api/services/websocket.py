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
from typing import List

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

def user_connected(sid: str) -> None:
  """Ajoute un utilisateur à la liste pour le compteurs.

  Arguments:
    sid (str): L'identifiant du socket.
  """
  global users, count
  if not sid in users:
    users.append(sid)
    count += 1

def user_disconnected(sid: str) -> None:
  """Retire un utilisateur de la liste pour le compteurs.

  Arguments:
    sid (str): L'identifiant du socket.
  """
  global users, count
  if sid in users:
    users.remove(sid)
    count -= 1

# Liste des utilisateurs connectés.
users: List[str] = []

# Nombre d'utilisateurs connectés.
count: int = 0

# Objet contenant le serveur de l'API REST.
websocket: AsyncServer = __init_asyncserver()