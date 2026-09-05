"""
Nom du module         : unicast.py
Description           : 
  Module gérant une boucle de diffusion pour un groupe de WebSocket avec des 
  données personnalisées pour chaque WebSocket.

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
  
  Contrairement à Socket.IO qui retire automatiquement un WebSocket qui se déconnecte de
  toutes les rooms dont il fait partie, il faut le retirer manuellement lors de 
  l'événement "disconnect" en appelant "cleanup_sid".
"""

from __future__ import annotations
from services.websocket import websocket
from libraries.response import Response
from asyncio import Task, CancelledError, sleep, create_task
from typing import Callable, Optional, Awaitable, List
from types import CoroutineType

# Type des fonctions à exécuter.
type UniTask = Callable[[str], Awaitable[Response]]

class UniCast():
  """Gère une boucle de diffusion pour un groupe de WebSocket avec des données personnalisées 
  pour chaque WebSocket."""

  # Liste de toutes les listes de diffusion.
  __actives: List[UniCast] = []
  
  def __init__(self, name: str, callback: UniTask, interval: Optional[float] = 1.0) -> None:
    """Constructeur de la classe.

    Arguments:
      name (str): Nom de la boucle de diffusion.
      callback (UniTask): Fonction retournant les données à diffuser.
      interval (Optional[float]): Nombre de secondes entre chaque diffusion. Par défaut à 1.0.
    """
    self.__start_name: str = f"{name}#follow"
    self.__stop_name: str = f"{name}#unfollow"
    self.__data_name: str = f"{name}#receive"
    self.__callback: UniTask = callback
    self.__interval: float = interval
    self.__tasks: dict[str, Task] = {}
    self.__register_events()
    UniCast.__actives.append(self)
  
  def __delete_sid(self, sid: str) -> None:
    """Supprime un WebSocket de la boucle de diffusion.

    Arguments:
      sid (str): ID du WebSocket à supprimer.
    """
    if sid in self.__tasks:
      self.__tasks[sid].cancel()
      del self.__tasks[sid]
  
  def __create_sid(self, sid: str) -> None:
    """Ajoute un WebSocket à la boucle de diffusion.

    Arguments:
      sid (str): ID du WebSocket à ajouter.
    """
    if sid not in self.__tasks:
      routine: CoroutineType = self.__stream_sid(sid)
      self.__tasks[sid] = create_task(routine)

  async def __stream_sid(self, sid: str) -> None:
    """Tâche d'exécution pour un WebSocket unique.

    Arguments:
      sid (str): ID du WebSocket pour la tâche.
    """
    try:
      while True:
        data: Response = await self.__callback(sid)
        await websocket.emit(self.__data_name, data, to=sid)
        await sleep(self.__interval)
    except CancelledError: pass

  def __register_events(self):
    """Enregistre les différents événements."""
    @websocket.on(self.__start_name)
    async def start(sid: str) -> None: 
      self.__create_sid(sid)
      
    @websocket.on(self.__stop_name)
    async def stop(sid: str) -> None: 
      self.__delete_sid(sid)
  
  @classmethod
  def cleanup_sid(cls, sid: str) -> None:
    """Retire un WebSocket de toutes les listes de diffusion lors de sa déconnexion."""
    for unicast in cls.__actives:
      unicast.__delete_sid(sid)