# home blueprint stuff
from flask import Blueprint, render_template
from flask import current_app

blueprint_home = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')
@blueprint_home.route('/', methods=['GET'])
def home():
    pass
    return render_template() #skeleton no template yet
