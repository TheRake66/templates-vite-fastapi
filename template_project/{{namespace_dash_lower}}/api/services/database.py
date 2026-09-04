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

from services.configuration import configuration, Json
from libraries.autoload import import_all
from libraries.ormbase import OrmBase
from sqlalchemy import create_engine, Engine
from typing import Any, Optional, Dict

def __get_sqlite(dbconf: Json) -> str:
  """Retourne l'URL de connexion pour SQLite.

  Arguments:
    dbconf (Json): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  return "sqlite:///:memory:" if dbconf["memory"] else \
        f"sqlite:///{dbconf["dbpath"]}"

def __get_remote(dbconf: Json) -> str:
  """Retourne l'URL de connexion pour une base distante.

  Arguments:
    dbconf (Json): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  remote: Json = dbconf["remote"]
  credential: str = f"{remote["username"]}:{remote["password"]}"
  connection: str = f"{remote["address"]}:{remote["port"]}"
  return f"{remote["driver"]}://{credential}@{connection}/{dbconf["dbpath"]}"

# Objet contenant la connexion à la base de données.
database: Optional[Engine] = None

# Initialise la connexion premier import.
if not database:
  dbconf: Json = configuration["database"]
  
  # Récupération de l'URL de connexion.
  url: str = \
    __get_sqlite(dbconf) if dbconf["sqlite"] else \
    __get_remote(dbconf)
  
  # Connexion à la base de données.
  database = create_engine(url, echo=dbconf["debug"])
  
  # Création des tables.
  if dbconf["create"]:
    import_all("bases")
    OrmBase.metadata.create_all(database)