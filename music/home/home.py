# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app

from music.domainmodel.track import Track
from music.tracks_bp.track_methods import csvreader_track_methods_extension

blueprint_home = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')
track_methods = csvreader_track_methods_extension()


@blueprint_home.route('/', methods=['GET'])
@blueprint_home.route('/home', methods=['GET'])
def home():
    return render_template('home.html', track_number=len(track_methods.dataset_of_tracks),
                           artist_number=len(track_methods.dataset_of_albums),
                           album_number=len(track_methods.dataset_of_artists),
                           genre_number=len(track_methods.dataset_of_genres))
