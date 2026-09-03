"""
Nom du module         : {{lower_name}}.py
Chemin du package     : {{namespace_dash_lower}}
Description           : 

Auteur                : {{user_name}}
Date de création      : {{datetime_full}}
Dernière modification : {{datetime_full}}
Version               : 1.0.0
Licence               : {{licence_name}}

Notes                 : 
"""

from api.libraries.ormbase import OrmBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class {{title_name}}(OrmBase):
  """Schéma de la table {{title_name}}."""
  
  __tablename__ = "{{lower_name}}"
  
  id: Mapped[int] = mapped_column(primary_key=True)