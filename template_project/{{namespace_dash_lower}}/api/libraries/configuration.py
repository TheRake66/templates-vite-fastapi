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

from __future__ import annotations
from typing import Dict, List, Union
from json import load

# Type d'un objet JSON.
type JsonValue = Union[str, int, float, bool, None]
type Json = Union[JsonValue, List[Json], Dict[str, Json]]

# Dictionnaire de la configuration de FastAPI.
with open("fastapi.json") as buffer:
  configuration: Json = load(buffer)