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
from pathlib import Path
from json import load

__FILE_NAME: str = "configuration.json"
"""Nom du fichier de configuration."""

type JsonValue = Union[str, int, float, bool, None]
"""Type d'une valeur JSON."""

type Json = Union[JsonValue, List[Json], Dict[str, Json]]
"""Type d'un objet JSON."""

configuration: Json = load(Path(__FILE_NAME).read_text())
"""Dictionnaire contenant la configuration."""