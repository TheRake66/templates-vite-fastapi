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
from yaml import safe_load
from pathlib import Path

__FILE_NAME: str = "config.yaml"
"""Nom du fichier de configuration."""

type YamlValue = Union[str, int, float, bool, None]
"""Type d'une valeur Yaml."""

type Yaml = Union[YamlValue, List[Yaml], Dict[str, Yaml]]
"""Type d'un objet Yaml."""

configuration: Yaml = safe_load(Path(__FILE_NAME).read_text("utf-8"))
"""Dictionnaire contenant la configuration."""