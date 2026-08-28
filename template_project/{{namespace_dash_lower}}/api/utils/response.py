"""
Nom du module         : response.py
Description           : Module gérant le format des réponses de l'API.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from pydantic import BaseModel

class Response(BaseModel):    
  """Représente la structure standard d'une réponse API.

  Attributes:
      message (str): Un message descriptif concernant le résultat de la requête.
      code (int): Le code de statut ou code d'erreur associé. Par défaut à 0.
      content (dict | None): Les données utiles renvoyées par l'opération. Par défaut à None.
  """
  message: str
  code: int = 0
  content: dict | None = None