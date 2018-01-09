from flask_cache import Cache

from app.app import app

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
