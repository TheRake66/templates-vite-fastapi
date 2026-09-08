"""
Nom du module         : broadcast.py
Description           : Module gérant une boucle de diffusion pour tous les WebSockets.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
  Pour utiliser une liste de diffusion dans le front, il suffit d'enregistrer
  l'événement "name#broadcast".
  
  Pour éviter de surcharger uniquement le serveur, on coupe toutes les listes de diffusion
  si aucun utilisateur n'est connecté. Il suffit d'utiliser "start_all" lors de l'événement 
  "connect" et "stop_all" lors de l'événement "disconnect".
"""

from libraries.response import Response
from services.websocket import emit_data
from asyncio import Task, CancelledError, sleep, create_task
from typing import Callable, Awaitable, List, Optional
from types import CoroutineType

# Type des fonctions à exécuter.
type BroadTask = Callable[[], Awaitable[Response]]

class BroadCast():
  """Gère une boucle de diffusion pour tous les WebSockets."""

  # Liste de toutes les listes de diffusion.
  __actives: List[BroadCast] = []
  
  def __init__(self, name: str, callback: BroadTask, interval: float = 1.0) -> None:
    """Constructeur de la classe.

    Arguments:
      name (str): Nom de la boucle de diffusion.
      callback (BroadTask): Fonction retournant les données à diffuser.
      interval (float): Nombre de secondes entre chaque diffusion. Par défaut à 1.0.
    """
    self.__event: str = f"{name}#broadcast"
    self.__callback: BroadTask = callback
    self.__interval: float = interval
    self.__task: Optional[Task] = None
    BroadCast.__actives.append(self)
  
  def __start_task(self) -> None:
    """Lance la tâche pour la boucle."""
    routine: CoroutineType = self.__stream_loop()
    self.__task = create_task(routine)
  
  def __stop_task(self) -> None:
    """Arrête la tâche pour la boucle."""
    self.__task.cancel()

  async def __stream_loop(self) -> CoroutineType:
    """Tâche d'exécution pour les WebSockets.

    Returns:
      CoroutineType: Coroutine asynchrone.
    """
    try:
      while True:
        data: Response = await self.__callback()
        await emit_data(self.__event, data)
        await sleep(self.__interval)
    except CancelledError: pass
  
  @classmethod
  def start_all(cls) -> None:
    """Lance toutes les tâches si utilisateur est connecté."""
    for unicast in cls.__actives:
      unicast.__start_task()
  
  @classmethod
  def stop_all(cls) -> None:
    """Arrête toutes les tâches si aucun utilisateur n'est connecté."""
    for unicast in cls.__actives:
      unicast.__stop_task()