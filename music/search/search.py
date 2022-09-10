# home blueprint stuff
from flask import Blueprint, render_template


blueprint_search = Blueprint('search_page', __name__, template_folder='templates', static_folder='static')


@blueprint_search.route('/search', methods=['GET'])
def search():
    return render_template('search.html')
