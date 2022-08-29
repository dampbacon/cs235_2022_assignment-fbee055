"""Initialize Flask app."""

from flask import Flask, render_template

# TODO: Access to the tracks should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!


# TODO: Access to the tracks should be implemented via the repository pattern and using blueprints, so this can not
#  stay here!


def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def home():
    #     some_track = create_some_track()
    #     # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
    #     return render_template('simple_track.html', track=some_track)
    #
    # return app
    with app.app_context():
        from .home import home
        from .tracks_bp import tracks_bp

        app.register_blueprint(home.blueprint_home)
        app.register_blueprint(tracks_bp.blueprint_track)

        return app
