from flask import Blueprint, render_template, redirect, url_for, session, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from password_validator import PasswordValidator
from functools import wraps

import music.authentication_bp.services as services
import music.adapters.repository as repo

# Configure Blueprint.
authentication_blueprint = Blueprint(
    'authentication_bp', __name__, url_prefix='/authentication')


@authentication_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    user_name_not_unique = None

    if form.validate_on_submit():
        user_name = form.user_name.data
        password = form.password.data

        try:
            services.add_user(user_name, password, repo.repo_instance)
            return redirect(url_for('authentication_bp.login'))
        except services.NameNotUniqueException:
            user_name_not_unique = 'User name not unique - please choose another name'
    return render_template(
        'credentials.html',
        title='Register',
        form=form,
        user_name_error_message=user_name_not_unique,
        handler_url=url_for('authentication_bp.register')
    )


@authentication_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user_name_not_recognised = None
    password_does_not_match_user_name = None

    if form.validate_on_submit():

        try:
            user = services.get_user(form.user_name.data, repo.repo_instance)

            # Authenticate User
            services.authenticate_user(user['user_name'], form.password.data, repo.repo_instance)

            # Initialise session and redirect to homepage
            session.clear()
            session['user_name'] = user['user_name']
            session['isLoggedIn'] = True
            return redirect(url_for('home_page.home'))

        except services.UnknownUserException:
            user_name_not_recognised = 'User name not recognised'
        except services.AuthenticationException:
            password_does_not_match_user_name = 'Password does not match user name'

    return render_template(
        'credentials.html',
        title='Login',
        form=form,
        user_name_error_message=user_name_not_recognised,
        password_error_message=password_does_not_match_user_name
    )


@authentication_blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home_page.home'))

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_name' not in session:
            return redirect(url_for('authentication_bp.login'))
        return view(**kwargs)

    return wrapped_view


class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must be at least 8 characters, and contain an upper case letter,\
            a lower case letter and a digit'
        self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(8) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    user_name = StringField('Username', [
        DataRequired(message='Your user name is required'),
        Length(min=3, message='Your user name is too short')])
    password = PasswordField('Password', [
        DataRequired(message='Your password is required'),
        PasswordValid()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    user_name = StringField('Username', [
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired()])
    submit = SubmitField('Login')
