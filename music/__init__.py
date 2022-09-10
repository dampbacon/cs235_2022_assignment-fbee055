"""Initialize Flask app."""
from pathlib import Path
from flask import Flask
# import adapters.repository as repo
# from adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    app = Flask(__name__)
    app.debug = True
    # app.config.from_object('config.Config')
    # data_path = Path('music') / 'adapters' / 'data'

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    with app.app_context():
        from .home import home
        from .tracks_bp import tracks_bp

        app.register_blueprint(home.blueprint_home)
        app.register_blueprint(tracks_bp.blueprint_track)
        # app.register_blueprint(login_bp.blueprint_login)
        return app
