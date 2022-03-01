from flask import Flask
from config.config import Config
def create_app(config_class=Config):
    app = Flask(__name__,template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    app.app_context().push()
    from controllers.main import index
    app.register_blueprint(index)
    return app
