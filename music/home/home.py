# home blueprint stuff
from flask import Blueprint, render_template
from music.tracks_bp.tracks_bp import track_methods

blueprint_home = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')
import music.adapters.repository as repo


@blueprint_home.route('/', methods=['GET'])
@blueprint_home.route('/home', methods=['GET'])
def home():
    print(len(repo.repo_instance.tracks))
    return render_template('home.html', track_number=len(repo.repo_instance.tracks),
                           album_number=len(repo.repo_instance.albums),
                           artist_number=len(repo.repo_instance.artists)
                           , genre_number=len(repo.repo_instance.genres))
