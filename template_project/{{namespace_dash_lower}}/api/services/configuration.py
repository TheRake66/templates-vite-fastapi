"""
Nom du module         : configuration.py
Description           : Module gérant la configuration de l'API.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from typing import Optional, Dict, List, Union
import json

# Type d'un objet JSON.
type Json = Dict[str, Union[str, int, float, bool, List, Dict, None]]

# Dictionnaire de la configuration de FastAPI.
configuration: Optional[Json] = None

# Charge la configuration premier import.
if not configuration:
  with open("fastapi.json") as buffer:
    configuration = json.load(buffer)