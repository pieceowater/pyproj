# api/__init__.py
from .server import app


@app.route('/')
def index():
    return app.name, 200


