"""
Nom du module         : ormbase.py
Description           : Module gérant les métadonnées des tables de données.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from sqlalchemy.orm import DeclarativeBase

class OrmBase(DeclarativeBase):
  """Représente le stockage métadonnées des tables de données."""
  pass