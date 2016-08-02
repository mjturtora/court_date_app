import os

def base(*path):
   return os.path.abspath(os.path.join(os.path.dirname(__file__), *path))

