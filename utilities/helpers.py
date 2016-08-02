import os

# save for later: sys.stderr.write('foo\n')

def base(*path):
   return os.path.abspath(os.path.join(os.path.dirname(__file__), *path))

