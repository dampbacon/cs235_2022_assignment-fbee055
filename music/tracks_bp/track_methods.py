# This file is gonna hold the methods needed for finding next and previous track required for browsing to work
#
from music.domainmodel.track import Track
from music.adapters.csvdatareader import TrackCSVReader

reader_obj = TrackCSVReader('tests/data/raw_albums_test.csv', 'tests/data/raw_tracks_test.csv')
reader_obj.read_csv_files()
tracks = reader_obj.dataset_of_tracks


def create_some_track():
    some_track = Track(1, "Heat Wavesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas")
    some_track.track_duration = 250
    some_track.track_url = 'https://spotify/track/1'
    return some_track


def find_track(track_id):
    for i in tracks:
        if i.track_id == track_id:
            return i


def get_next_track():
    pass


def get_previous_track():
    pass


def get_first_track():
    pass


def get_last_track():
    pass


def get_track_data():
    pass
