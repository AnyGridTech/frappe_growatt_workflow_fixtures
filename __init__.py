import os

# Expose inner package directory so imports find module files
__path__.insert(0, os.path.join(os.path.dirname(__file__), __name__))
