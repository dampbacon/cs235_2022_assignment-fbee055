
import music.adapters.repository as repo

from flask import Blueprint, render_template, redirect, url_for, session, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from better_profanity import profanity
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from password_validator import PasswordValidator
from functools import wraps

from music.authentication_bp.authentication import login_required
import music.tracks_bp.track_table_methods as track_table
# test search code
from music.search.search_methods import search_by_album_name, search_by_track_name

blueprint_track = Blueprint('tracks_page', __name__, template_folder='templates', static_folder='static')

track_methods = repo.repo_instance
tracks = track_methods.tracks


@blueprint_track.route('/track', methods=['GET'])
def display_track():
    return redirect(url_for('tracks_page.display_track_at_id', track_id=tracks[0].track_id) + '?order=tracks')


@blueprint_track.route('/track/<int:track_id>', methods=['get'])
def display_track_at_id(track_id=None):
    query_params = ''
    args = request.args
    list_from_query = tracks
    bookmarks = None
    if 'order' in args:
        if args['order'] in ['tracks', 'albums', 'artists']:
            query_params = '?order=' + args['order']
            if args['order'] == 'albums':
                list_from_query = track_methods.tracks_a
                bookmarks = track_methods.create_bookmarks(list_from_query, 1)

            elif args['order'] == 'tracks':
                list_from_query = track_methods.tracks_t
                bookmarks = track_methods.create_bookmarks(list_from_query, 0)

            elif args['order'] == 'artists':
                list_from_query = track_methods.tracks_artist
                bookmarks = track_methods.create_bookmarks(list_from_query, 2)
            
            elif args['order'] == 'genres':
                print("genre sorted!")
                list_from_query = track_methods.tracks_genre
                bookmarks = track_methods.create_bookmarks(list_from_query, 3)
    print(bookmarks)
    print(search_by_track_name(track_methods,'love'))
    track_data = track_methods.find_track(list_from_query, track_id)
    np_url_id_tuple = track_methods.get_next_and_previous_track(list_from_query, track_data)
    return render_template('display_track.html', track=track_data[0], np_tuple=np_url_id_tuple,
                           first=track_methods.get_first_track(list_from_query),
                           last=track_methods.get_last_track(list_from_query),
                           bookmarks=bookmarks, query_params=query_params, genre_list=track_data[0].genres)


@blueprint_track.route('/track/<int:track_id>/sort_by_album', methods=['get'])
def sort_by_album_button(track_id=None):
    return redirect(url_for('tracks_page.display_track_at_id', track_id=track_id) + '?order=albums')


@blueprint_track.route('/track/<int:track_id>/sort_by_track_name', methods=['get'])
def sort_by_track_name_button(track_id=None):
    return redirect(url_for('tracks_page.display_track_at_id', track_id=track_id) + '?order=tracks')


@blueprint_track.route('/track/<int:track_id>/sort_by_artist_name', methods=['get'])
def sort_by_artist_button(track_id=None):
    return redirect(url_for('tracks_page.display_track_at_id', track_id=track_id) + '?order=artists')

@blueprint_track.route('/track/<int:track_id>/sort_by_genre', methods=['get'])
def sort_by_genres(track_id=None):
    return redirect(url_for('tracks_page.display_track_at_id', track_id=track_id) + '?order=genres')


@blueprint_track.route('/track/list', methods=['get'])
def data_tables_list():
    return render_template('tracks_datatables_list.html')


@blueprint_track.route('/track/list/api/data', methods=['get'])
def data_tables_list_data():
    return {'data': [track_table.track_obj_to_dict(track_i) for track_i in track_methods.tracks]}

@blueprint_track.route('/comment', methods=['GET', 'POST'])
@login_required
def comment_on_track():
    # Obtain the user name of the currently logged in user.
    user_name = session['user_name']

    # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
    # the form with an article id, when subsequently called with a HTTP POST request, the article id remains in the
    # form.
    form = CommentForm()

    if form.validate_on_submit():
        # Successful POST, i.e. the comment text has passed data validation.
        # Extract the article id, representing the commented article, from the form.
        article_id = int(form.article_id.data)

        # Use the service layer to store the new comment.
        ##services.add_comment(article_id, form.comment.data, user_name, repo.repo_instance)

        # Retrieve the article in dict form.
        ##article = services.get_article(article_id, repo.repo_instance)

        # Cause the web browser to display the page of all articles that have the same date as the commented article,
        # and display all comments, including the new comment.
        return redirect(url_for('news_bp.articles_by_date', date=article['date'], view_comments_for=article_id))

    if request.method == 'GET':
        # Request is a HTTP GET to display the form.
        # Extract the article id, representing the article to comment, from a query parameter of the GET request.
        article_id = int(request.args.get('article'))

        # Store the article id in the form.
        form.article_id.data = article_id
    else:
        # Request is a HTTP POST where form validation has failed.
        # Extract the article id of the article being commented from the form.
        article_id = int(form.article_id.data)

    # For a GET or an unsuccessful POST, retrieve the article to comment in dict form, and return a Web page that allows
    # the user to enter a comment. The generated Web page includes a form object.
    article = services.get_article(article_id, repo.repo_instance)
    return render_template(
        'news/comment_on_article.html',
        title='Edit article',
        article=article,
        form=form,
        handler_url=url_for('news_bp.comment_on_article'),
        selected_articles=utilities.get_selected_articles(),
        tag_urls=utilities.get_tags_and_urls()
    )

class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    article_id = HiddenField("Article id")
    submit = SubmitField('Submit')