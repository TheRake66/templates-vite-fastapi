"""
Nom du module         : multicast.py
Description           : Module gérant une boucle de diffusion pour un groupe de WebSocket.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
  Pour utiliser une liste de diffusion dans le front, il suffit d'enregistrer
  les événements :
    - name#follow : Enregistre le WebSocket dans la boucle de diffusion.
    - name#unfollow : Retire le WebSocket dans la boucle de diffusion.
    - name#receive : Envoie les données de la boucle de diffusion vers le WebSocket.
"""

from api.services.websocket import websocket
from api.libraries.response import Response
from asyncio import Task, CancelledError, sleep, create_task
from typing import Callable, Optional
from types import CoroutineType

# Type des fonctions à exécuter.
type MultiTask = Callable[[], Response]

class MultiCast():
  """Gère une boucle de diffusion pour un groupe de WebSocket."""
  
  def __init__(self, name: str, callback: MultiTask, interval: Optional[float] = 1.0) -> None:
    """Constructeur de la classe.

    Arguments:
      name (str): Nom de la boucle de diffusion.
      callback (MultiTask): Fonction retournant les données à diffuser.
      interval (Optional[float]): Nombre de secondes entre chaque diffusion. Par défaut à 1.0.
    """
    self.__room: str = name
    self.__follow: str = f"{name}#follow"
    self.__unfollow: str = f"{name}#unfollow"
    self.__receive: str = f"{name}#receive"
    self.__callback: MultiTask = callback
    self.__interval: float = interval
    self.__task: Optional[Task] = None
    self.__count: int = 0
    self.__register_events()
  
  def __enter_room(self, sid: str) -> None:
    """Ajoute un WebSocket à la boucle de diffusion.

    Arguments:
      sid (str): ID du WebSocket à ajouter.
    """
    websocket.enter_room(sid, self.__room)
    self.__count += 1
    if self.__count == 1:
      routine: CoroutineType = self.__stream_room()
      self.__task = create_task(routine)
      
  def __leave_room(self, sid: str) -> None:
    """Supprime un WebSocket de la boucle de diffusion.

    Arguments:
      sid (str): ID du WebSocket à supprimer.
    """
    websocket.leave_room(sid, self.__room)
    self.__count -= 1
    if self.__count == 0:
      self.__task.cancel()

  async def __stream_room(self) -> None:
    """Tâche d'exécution pour les WebSockets."""
    try:
      while True:
        data: Response = await self.__callback()
        await websocket.emit(self.__receive, data, room=self.__room)
        await sleep(self.__interval)
    except CancelledError: pass
  
  def __register_events(self):
    """Enregistre les différents événements."""
    @websocket.on(self.__follow)
    async def start(sid: str) -> None: 
      self.__enter_room(sid)
      
    @websocket.on(self.__unfollow)
    async def leave(sid: str): 
      self.__leave_room(sid)