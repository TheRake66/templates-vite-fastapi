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
"""

from services.websocket import websocket
from libraries.response import Response
from asyncio import sleep, create_task
from typing import Callable, Optional

# Type des fonctions à exécuter.
type BroadTask = Callable[[], Response]

class BroadCast():
  """Gère une boucle de diffusion pour tous les WebSockets."""
  
  def __init__(self, name: str, callback: BroadTask, interval: Optional[float] = 1.0) -> None:
    """Constructeur de la classe.

    Arguments:
      name (str): Nom de la boucle de diffusion.
      callback (BroadTask): Fonction retournant les données à diffuser.
      interval (Optional[float]): Nombre de secondes entre chaque diffusion. Par défaut à 1.0.
    """
    self.__event: str = f"{name}#broadcast"
    self.__callback: BroadTask = callback
    self.__interval: float = interval
    create_task(self.__stream_loop())

  async def __stream_loop(self) -> None:
    """Tâche d'exécution pour les WebSockets."""
    while True:
      data: Response = await self.__callback()
      await websocket.emit(self.__event, data, broadcast=True)
      await sleep(self.__interval)