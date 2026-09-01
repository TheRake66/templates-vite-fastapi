"""
Nom du module         : database.py
Description           : Module gérant la connexion à la base de données.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from api.utils.configuration import configuration
from sqlalchemy import create_engine, Engine
from typing import Any

def __get_sqlite(database: dict[str, Any]) -> str:
  """Retourne l'URL de connexion pour SQLite.

  Arguments:
    database (dict[str, Any]): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  return f"sqlite://{database["pathto"]}"

def __get_remote(database: dict[str, Any]) -> str:
  """Retourne l'URL de connexion pour une base distante.

  Arguments:
    database (dict[str, Any]): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  remote: dict = database["remote"]
  credential: str = f"{remote["username"]}:{remote["password"]}"
  connection: str = f"{remote["address"]}:{remote["port"]}"
  return f"{remote["driver"]}://{credential}@{connection}/{database["pathto"]}"

# Objet contenant la connexion à la base de données.
engine: Engine | None = None

# Initialise la connexion premier import.
if not engine:
  database: dict[str, Any] = configuration["database"]
  if database["enable"]:
    url: str = \
      __get_sqlite(database) if database["sqlite"] else \
      __get_remote(database)
    engine = create_engine(url)



