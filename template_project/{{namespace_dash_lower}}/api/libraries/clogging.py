"""
Nom du module         : clogging.py
Description           : Module gérant le système de journalisation.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from logging import Logger, getLogger, DEBUG, Formatter, StreamHandler, FileHandler

__FILE_NAME: str = "logging.log"
"""Nom du fichier de journalisation."""

def __init_logger() -> Logger:
  """Retourne le système de journalisation.

  Returns:
    Logger: Le système de journalisation.
  """
  # Initialise le système de journalisation.
  logger: Logger = getLogger("clogging")
  logger.propagate = False
  logger.setLevel(DEBUG)
  formatter = Formatter("".join([
    "[%(process)d] ",
    "[%(asctime)s] ",
    "[%(levelname)s] ",
    "[%(module)s:%(funcName)s:%(lineno)d] ",
    "%(message)s"]),
    "%Y-%m-%d %H:%M:%S" )

  # Affiche dans la console.
  console: StreamHandler = StreamHandler()
  console.setFormatter(formatter)
  logger.addHandler(console)
  
  # Ajoute dans un fichier.
  file: FileHandler = FileHandler(__FILE_NAME, encoding="utf-8")
  file.setFormatter(formatter) 
  logger.addHandler(file)
  
  # Retourne le système de journalisation.
  return logger

logger: Logger = __init_logger()
"""Objet contenant le système de journalisation."""