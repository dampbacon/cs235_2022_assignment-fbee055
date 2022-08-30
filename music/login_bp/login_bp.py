from flask import Blueprint

blueprint_login = Blueprint('login_page', __name__, template_folder='templates', static_folder='static')


@blueprint_login.route('/login', methods=['GET'])
def login_pg():
    pass
