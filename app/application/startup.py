import falcon

from .config import STATIC_PATH
from .view import ShufflerViewV1
from .docs import add_docs


api = falcon.API()

api.add_route('/v1/shuffler', ShufflerViewV1())
api.add_static_route('/static', STATIC_PATH)
add_docs('/v1/docs', '/static/schema-v1.json', app=api)


__all__ = ('api',)
