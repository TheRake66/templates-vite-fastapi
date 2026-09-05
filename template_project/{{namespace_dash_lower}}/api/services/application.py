"""
Nom du module         : application.py
Description           : Module gérant l'application principale.

Auteur                : TheRake66
Date de création      : 2026-08-28 04:01:51
Dernière modification : 2026-08-28 04:01:51
Version               : 1.0.0
Licence               : GPL-3.0

Notes                 : 
"""

from libraries.configuration import configuration, Json
from services.websocket import websocket
from services.apirest import apirest
from socketio import ASGIApp

def __init_asgiapp() -> ASGIApp:
  """Initialise le service ASGIApp.

  Returns:
    ASGIApp: Le service ASGIApp.
  """
  # Chargement de la configuration.
  config: Json = configuration["websocket"]
  
  # Définition du serveur.
  application: ASGIApp = ASGIApp(
    socketio_server=websocket,
    other_asgi_app=apirest,
    socketio_path=config["urlpath"])
  
  # On retourne le service.
  return application

# Objet contenant le serveur de l'application.
application: ASGIApp = __init_asgiapp()