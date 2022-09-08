"""Initialize Flask app."""

from flask import Flask

from music.login_bp import login_bp


def create_app():
    app = Flask(__name__)
    app.debug = True

    with app.app_context():
        from .home import home
        from .tracks_bp import tracks_bp

        app.register_blueprint(home.blueprint_home)
        app.register_blueprint(tracks_bp.blueprint_track)
        app.register_blueprint(login_bp.blueprint_login)
        return app
