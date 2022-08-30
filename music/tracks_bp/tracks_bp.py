# tracks and track displaying stuff
# tracks and tracks displaying stuff
# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app
from music.tracks_bp.track_methods import *

blueprint_track = Blueprint('tracks_page', __name__, template_folder='templates', static_folder='static')


@blueprint_track.route('/track', methods=['GET'])
def display_track():
    a = tracks[2]
    print(tracks)
    return render_template('display_track.html', track=a)


@blueprint_track.route('/track/<int:track_id>', methods=['get'])
def display_track_at_id(track_id=None):
    track_data = find_track(track_id)
    print("track data:", track_data[0])
    np_url_id_tuple = get_next_and_previous_track(track_data)
    print(tracks)
    print(np_url_id_tuple, '   prev=', np_url_id_tuple[0].track_id, '    next=', np_url_id_tuple[1].track_id)

    return render_template('display_track.html', track=track_data[0], np_tuple=np_url_id_tuple)
