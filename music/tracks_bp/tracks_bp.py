# tracks and track displaying stuff
# tracks and tracks displaying stuff
# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app
from music.tracks_bp.track_methods import *

blueprint_track = Blueprint('tracks_page', __name__, template_folder='templates', static_folder='static')


@blueprint_track.route('/track', methods=['GET'])
def display_track():
    a = create_some_track()
    print(tracks)
    return render_template('display_track.html', track=a)


@blueprint_track.route('/track/<int:track_id>', methods=['get'])
def display_track_at_id(track_id=None):
    return render_template('display_track.html', track=find_track(track_id))
