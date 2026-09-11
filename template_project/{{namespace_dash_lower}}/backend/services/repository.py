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

from libraries.configuration import configuration, Yaml
from fakeredis.aioredis import FakeRedis
from redis.asyncio import Redis
from typing import Union

def __init_manager() -> Union[Redis, FakeRedis]:
  """Initialise le service Manager.

  Returns:
    Union[Redis, FakeRedis]: Le service Manager.
  """
  # Chargement de la configuration.
  config: Yaml = configuration["repository"]
  
  # Définition du serveur.
  manager: Union[Redis, FakeRedis] = \
    FakeRedis(config["decode"]) if config["memory"] else \
    Redis(__url, config["decode"])

  # On retourne le service
  return manager

def __build_remote() -> str:
  """Construit et retourne l'URL de connexion pour un dépôt de cache distant.

  Returns:
    str: L'URL de connexion.
  """
  # Chargement de la configuration.
  remote: Yaml = configuration["repository"]["remote"]
  
  # On retourne l"URL construite.
  return "redis://{}:{}@{}:{}/{}".format(
    remote["username"], remote["password"],
    remote["address"], remote["port"],
    remote["index"])

def get_remote() -> str:
  """Retourne l'URL de connexion pour un dépôt de cache distant.

  Returns:
    str: L'URL de connexion.
  """
  return __url

__url: str = __build_remote()
"""L'URL de connexion pour un dépôt de cache distant."""

manager: Union[Redis, FakeRedis] = __init_manager()
"""Objet contenant la connexion au dépôt de cache."""