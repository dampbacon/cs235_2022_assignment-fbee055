# home blueprint stuff
from flask import Blueprint, render_template
from music.tracks_bp.tracks_bp import track_methods


blueprint_home = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')
track_methods = track_methods


@blueprint_home.route('/', methods=['GET'])
@blueprint_home.route('/home', methods=['GET'])
def home():
    return render_template('home.html', track_number=len(track_methods.dataset_of_tracks),
                           artist_number=len(track_methods.dataset_of_albums),
                           album_number=len(track_methods.dataset_of_artists),
                           genre_number=len(track_methods.dataset_of_genres))
