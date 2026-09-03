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

from api.utils.configuration import config
from api.utils.autoload import import_all
from api.utils.ormbase import OrmBase
from sqlalchemy import create_engine, Engine
from typing import Any, Optional

def __get_sqlite(database: dict[str, Any]) -> str:
  """Retourne l'URL de connexion pour SQLite.

  Arguments:
    database (dict[str, Any]): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  return "sqlite:///:memory:" if database["memory"] else \
        f"sqlite:///{database["dbpath"]}"

def __get_remote(database: dict[str, Any]) -> str:
  """Retourne l'URL de connexion pour une base distante.

  Arguments:
    database (dict[str, Any]): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  remote: dict[str, Any] = database["remote"]
  credential: str = f"{remote["username"]}:{remote["password"]}"
  connection: str = f"{remote["address"]}:{remote["port"]}"
  return f"{remote["driver"]}://{credential}@{connection}/{database["dbpath"]}"

def __create_all(engine: Engine) -> None:
  """Charge tous les modules des tables, puis les crée de la base de données.

  Arguments:
    database (dict[str, Any]): La connexion à la base de données.
  """
  import_all("api/bases")
  OrmBase.metadata.create_all(engine)

# Objet contenant la connexion à la base de données.
engine: Optional[Engine] = None

# Initialise la connexion premier import.
if not engine:
  database: dict[str, Any] = config["database"]
  url: str = \
    __get_sqlite(database) if database["sqlite"] else \
    __get_remote(database)
  engine = create_engine(url, echo=database["debug"])
  if database["create"]: __create_all(engine)