from os.path import exists, join, dirname
from subprocess import check_call
from os import name, chdir
from sys import exit

VENV_DIR: str = "venv"
RUN_CMD: str = "uvicorn main:application --reload --host localhost --port 8000"

chdir(dirname(__file__))

if not exists(VENV_DIR): exit(1)

exe: str = (join(VENV_DIR, "bin", "python"), 
            join(VENV_DIR, "Scripts", "python.exe"))[name == "nt"]

if not exists(exe): exit(1)

check_call([exe, "-m"] + RUN_CMD.split())