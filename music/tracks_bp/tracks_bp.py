# tracks and track displaying stuff
# tracks and tracks displaying stuff
# home blueprint stuff
from flask import Blueprint, render_template, redirect, url_for
from flask import current_app
from music.tracks_bp.track_methods import *

blueprint_track = Blueprint('tracks_page', __name__, template_folder='templates', static_folder='static')

track_methods = csvreader_track_methods_extension()
tracks = track_methods.get_track_data()

@blueprint_track.route('/track', methods=['GET'])
def display_track():
    a = tracks[2]
    print(tracks)
    return render_template('display_track.html', track=a)


@blueprint_track.route('/track/<int:track_id>', methods=['get'])
def display_track_at_id(track_id=None):
    track_data = track_methods.find_track(track_id)
    # sort_by_track_name()
    # works should be moved later
    # sort_by_album_name()

    print("track data:", track_data[0])
    np_url_id_tuple = track_methods.get_next_and_previous_track(track_data)
    print('NP_URL_TUPLE_________: ', np_url_id_tuple)
    return render_template('display_track.html', track=track_data[0], np_tuple=np_url_id_tuple,
                           first=track_methods.get_first_track(),
                           last=track_methods.get_last_track(), bookmarks=track_methods.create_bookmarks(0))


@blueprint_track.route('/track/<int:track_id>/sort_by_album', methods=['get'])
def sort_by_album_button(track_id=None):
    track_methods.sort_by_album_name(False)
    return redirect(url_for('tracks_page.display_track_at_id', track_id=track_id))


@blueprint_track.route('/track/<int:track_id>/sort_by_track_name', methods=['get'])
def sort_by_track_name_button(track_id=None):
    track_methods.sort_by_track_name(False)
    a = track_methods.create_bookmarks(0)
    print('_______________________________________________ BOOKMARKS', a)
    return redirect(url_for('tracks_page.display_track_at_id', track_id=track_id))
