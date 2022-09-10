"""Initialize Flask app."""
from pathlib import Path
from flask import Flask
import music.adapters.repository as repo
from music.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object('config.Config')
    data_path = Path('music') / 'adapters' / 'data'

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        from .home import home
        app.register_blueprint(home.blueprint_home)

        from .tracks_bp import tracks_bp
        app.register_blueprint(tracks_bp.blueprint_track)

        from .authentication_bp import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from .search import search
        app.register_blueprint(search.blueprint_search)

    return app
