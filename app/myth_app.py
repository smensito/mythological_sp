from config import Config
from flask import Flask

myth_app = Flask(__name__)


def init_app():
    myth_app.config.from_object(Config)

    register_blueprints(myth_app)


def register_blueprints(app):
    from .views import routes
    app.register_blueprint(routes.routes)



