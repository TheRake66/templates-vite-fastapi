"""
Nom du module         : structure.py
Description           : 
  Module servant de base aux structures de parametres
  des requetes vers l'API.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from pydantic import BaseModel
from typing import Any

class Structure(BaseModel):
  """Représente la structure standard des paramètres d'une requête API."""
  
  def filter(self) -> dict[str, Any]:
    """Renvoi un dictionnaire d'attribut/valeur en retirantles attributs sans valeur.

    Returns:
      dict[str, Any]: Le dictionnaire filtré.
    """
    return self.model_dump(exclude_unset=True)