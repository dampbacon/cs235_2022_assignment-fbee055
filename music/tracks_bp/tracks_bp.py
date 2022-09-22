# tracks and track displaying stuff
# tracks and tracks displaying stuff
# home blueprint stuff
from flask import Blueprint, render_template, redirect, url_for, request, g
from flask import current_app
from music.tracks_bp.track_methods import *
from music.tracks_bp.track_table_methods import track_obj_to_dict

blueprint_track = Blueprint('tracks_page', __name__, template_folder='templates', static_folder='static')

track_methods = csvreader_track_methods_extension()
tracks = track_methods.get_track_data()


@blueprint_track.route('/track', methods=['GET'])
def display_track():
    return redirect(url_for('tracks_page.display_track_at_id', track_id=tracks[0].track_id))


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
    return {'data': [track_obj_to_dict(track_i) for track_i in track_methods.tracks]}
