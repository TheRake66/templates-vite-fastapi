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

from typing import Any, Optional, Dict
import json

# Dictionnaire de la configuration de FastAPI.
configuration: Optional[Dict[str, Any]] = None

# Charge la configuration premier import.
if not configuration:
  with open("api/fastapi.json") as buffer:
    configuration = json.load(buffer)