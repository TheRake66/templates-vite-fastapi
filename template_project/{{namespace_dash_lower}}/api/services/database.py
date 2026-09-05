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
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine
from collections.abc import Iterator
from typing import Optional

# Objet contenant la connexion à la base de données.
engine: Optional[Engine] = None

# Objet faisant le lien entre l'ORM et l'engine.
session: Optional[Session] = None

def __get_sqlite(config: Json) -> str:
  """Retourne l'URL de connexion pour SQLite.

  Arguments:
    config (Json): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  return "sqlite:///:memory:" if config["memory"] else \
        f"sqlite:///{config["dbpath"]}"

def __get_remote(config: Json) -> str:
  """Retourne l'URL de connexion pour une base distante.

  Arguments:
    config (Json): La configuration de la base de données.

  Returns:
    str: L'URL de connexion.
  """
  remote: Json = config["remote"]
  credential: str = f"{remote["username"]}:{remote["password"]}"
  connection: str = f"{remote["address"]}:{remote["port"]}"
  return f"{remote["driver"]}://{credential}@{connection}/{config["dbpath"]}"

def get_database() -> Iterator[Session]:
  """Crée un générateur pour les dépendances.

  Yields:
    Iterator[Session]: Une session de base de données.
  """
  database: Session = session()
  try: yield database
  finally: database.close()

# Initialise la connexion premier import.
if not engine and not session:
  config: Json = configuration["database"]

  # Récupération de l'URL de connexion.
  url: str = \
    __get_sqlite(config) if config["sqlite"] else \
    __get_remote(config)
  
  # Connexion à la base de données.
  engine = create_engine(url, echo=config["debug"])
  session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  
  # Création des tables.
  if config["create"]:
    import_all("bases")
    OrmBase.metadata.create_all(engine)