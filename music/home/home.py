# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app

from music.domainmodel.track import Track

blueprint_home = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')


# test code

@blueprint_home.route('/', methods=['GET'])
@blueprint_home.route('/home', methods=['GET'])
def home():
    #     # Use Jinja to customize a predefined html page rendering the layout for showing a single track.
    return render_template('home.html')
