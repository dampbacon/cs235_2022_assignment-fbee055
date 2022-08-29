#tracks and tracks displaying stuff
# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app

blueprint_track = Blueprint('tracks_page', __name__, template_folder='templates', static_folder='static')
@blueprint_track.route('/track', methods=['GET'])
def home():
    pass
    return render_template() #skeleton no template yet
