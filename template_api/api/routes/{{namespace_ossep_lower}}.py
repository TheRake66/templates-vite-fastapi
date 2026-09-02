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

from api.utils.response import Response
from api.utils.structure import Structure
from api.utils.database import engine
from fastapi import APIRouter
from typing import Optional

# Point d'entrée de l'API {{title_name}}.
router = APIRouter(prefix="/{{namespace_back_lower}}")

class {{title_name}}(Structure):
  """Schéma de données de {{title_name}}."""
  pass

@router.get("/")
async def hello_{{lower_name}}() -> Response:
  """Racine de l'entrée de l'API."""
  return Response(message="Bonjour depuis l'API {{title_name}}.")