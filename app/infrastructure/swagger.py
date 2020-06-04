from falcon_swagger_ui import register_swaggerui_app

from application.config import SWAGGER


def register_swagger(app, **kwargs):
    params = {
        **SWAGGER,
    }
    params.update(kwargs)
    register_swaggerui_app(app=app, **params)


__all__ = ('register_swagger',)
