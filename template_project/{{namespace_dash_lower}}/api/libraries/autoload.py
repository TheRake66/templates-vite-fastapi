"""
Nom du module         : autoload.py
Description           : Module gérant l'auto-import de module.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from importlib import import_module
from typing import Any, List, Optional
from types import ModuleType
from pathlib import Path

def import_all(package: str, varname: Optional[str] = None) -> List[Any]:
  """Importe récursivement tous les modules d'un dossier et retourne un tableau d'attributs.

  Arguments:
    package (str): Le chemin du dossier contenant les modules.
    varname (Optional[str]): Le nom de l'attribut à récupérer dans les modules. Aucun par défaut.

  Returns:
    List[Any]: Les valeurs des attributs si un nom a été passé.
  """
  values: List[Any] = []
  for file in Path(package).rglob("*.py"):
    module: str = ".".join(file.with_suffix("").parts)
    loaded: ModuleType = import_module(module)
    if varname: values += [getattr(loaded, varname)]
  return values


