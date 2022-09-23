# home blueprint stuff
from flask import Blueprint, render_template
import music.utilities.utilities as utilities

blueprint_search = Blueprint('search_page', __name__, template_folder='templates', static_folder='static')


@blueprint_search.route('/search', methods=['GET'])
def search():
    return render_template('search.html', genre_urls=utilities.get_genres_and_urls())
