from os.path import exists, join, dirname
from subprocess import check_call
from os import name, chdir
from sys import executable

VENV_DIR: str = "venv"
PACK_FILE: str = "requirements.txt"

chdir(dirname(__file__))

if not exists(VENV_DIR):
  check_call([executable, "-m", "venv", VENV_DIR])

bin: str = ("bin", "Scripts")[name == "nt"]
pip: str = join(VENV_DIR, bin, "pip")

if exists(PACK_FILE):
  check_call([pip, "install", "-r", PACK_FILE])