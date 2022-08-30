# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app

from music.domainmodel.track import Track

blueprint_home = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')



#test code
def create_some_track():
    some_track = Track(1, "Heat Waves")
    some_track.track_duration = 250
    some_track.track_url = 'https://spotify/track/1'
    return some_track


@blueprint_home.route('/', methods=['GET'])
@blueprint_home.route('/home', methods=['GET'])
def home():
    some_track = create_some_track()
    #     # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
    return render_template('simple_track.html', track=some_track)
