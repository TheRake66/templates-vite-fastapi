"""
Nom du module         : repository.py
Description           : Module gérant le serveur de dépôt de cache.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from libraries.configuration import configuration, Json
from fakeredis.aioredis import FakeRedis
from redis.asyncio import Redis
from typing import Union

def __init_manager() -> Union[Redis, FakeRedis]:
  """Initialise le service Manager.

  Returns:
    Union[Redis, FakeRedis]: Le service Manager.
  """
  # Chargement de la configuration.
  config: Json = configuration["repository"]
  
  # Définition du serveur.
  manager: Union[Redis, FakeRedis] = \
    FakeRedis(config["decode"]) if config["memory"] else \
    Redis(get_remote(), config["decode"])

  # On retourne le service
  return manager

def get_remote(config: Json) -> str:
  """Retourne l'URL de connexion pour un dépôt de cache distant.

  Arguments:
    config (Json): La configuration du dépôt de cache.

  Returns:
    str: L'URL de connexion.
  """
  remote: Json = config["remote"]
  return "redis://{}:{}@{}:{}/{}".format(
    remote["username"], remote["password"],
    remote["address"], remote["port"],
    remote["index"])

manager: Union[Redis, FakeRedis] = __init_manager()
"""Objet contenant la connexion au dépôt de cache."""