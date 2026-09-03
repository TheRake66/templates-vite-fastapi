"""
Nom du module         : websocket.py
Description           : Module gérant les WebSockets.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from typing import Callable, Awaitable, Any, Optional
from fastapi import WebSocket, WebSocketDisconnect

type WSCallback = Callable[[WebSocket], Awaitable[None]]
type WSReceiveCallback = Callable[[WebSocket, Any], Awaitable[None]]

async def handle_websocket(
  websocket: WebSocket,
  receive: WSReceiveCallback,
  connect: Optional[WSCallback] = None,
  disconnect: Optional[WSCallback] = None) -> None:
  """Gère la boucle d'un WebSocket.

  Arguments:
    websocket (WebSocket): Le WebSocket envoyé par FastAPI.
    receive (WSReceiveCallback): La fonction à exécuter lors de la réception de données.
    accept (Optional[WSCallback]): La fonction à exécuter lors de la connexion. Aucune par deféut.
    disconnect (Optional[WSCallback]): La fonction à exécuter lors de la déconnexion. Aucune par deféut.
  """
  await websocket.accept()
  if connect: await connect(websocket)
  try:
    while True:
      data: Any = await websocket.receive_json()
      await receive(websocket, data)
  except WebSocketDisconnect:
    if disconnect: await disconnect(websocket)