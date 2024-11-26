import os
from server.backend import backend, init_all

init_all()
application = backend

try:
    from whitenoise import WhiteNoise
    application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'static'))
except (ModuleNotFoundError, ImportError):
    pass

app = application
