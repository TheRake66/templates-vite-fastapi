"""
Nom du module         : {{lower_name}}.py
Chemin du package     : {{namespace_dash_lower}}
Description           : 

Auteur                : {{user_name}}
Date de création      : {{datetime_full}}
Dernière modification : {{datetime_full}}
Version               : 1.0.0
Licence               : {{licence_name}}

Notes                 : 
"""

from api.libraries.structure import Structure
from api.libraries.response import Response
from api.services.websocket import websocket
from typing import Any, Optional
from fastapi import APIRouter

# Point d'entrée de {{title_name}}.
NAMESPACE: str = "{{namespace_dash_lower}}"
URLPATH: str = "{{namespace_back_lower}}"
router: APIRouter = APIRouter(prefix=f"/{URLPATH}")

class {{title_name}}(Structure):
  """Schéma de données de {{title_name}}."""
  pass

@router.get("/hello")
async def hello_apirest() -> Response:
  """Fonction qui dit bonjour pour l'API REST."""
  return Response(message="Bonjour depuis l'API REST {{title_name}}.")

@websocket.on(f"{NAMESPACE}:hello")
async def hello_websocket() -> None:
  """Fonction qui dit bonjour pour le WebSocket."""
  await websocket.emit(f"{NAMESPACE}:hello", \
    Response(message="Bonjour depuis le WebSocket {{title_name}}."))