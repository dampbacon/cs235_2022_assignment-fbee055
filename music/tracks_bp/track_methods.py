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
            return i, tracks.index(i)


# def get_next_and_previous_track(current_track):
#     temp_list = [0, 0]
#     if current_track[0] != get_last_track():
#         print("WHAT IS WRONG. TRACK PREVIOUS", tracks[current_track[1] - 1])
#         temp_list[0] = tracks[current_track[1] - 1]
#     if current_track[0] != get_first_track():
#         print("WHAT IS WRONG. TRACK PREVIOUS", tracks[current_track[1] + 1])
#         temp_list[1] = tracks[current_track[1] + 1]
#     return tuple(temp_list)


def get_next_and_previous_track(current_track):
    temp_list = [0, 0]
    if current_track[0] == get_last_track():
        print("WHAT IS WRONG. TRACK PREVIOUS", tracks[current_track[1] - 1])
        temp_list[0] = tracks[current_track[1] - 1]
    elif current_track[0] == get_first_track():
        print("WHAT IS WRONG. TRACK PREVIOUS", tracks[current_track[1] + 1])
        temp_list[1] = tracks[current_track[1] + 1]
    elif current_track[0] != get_last_track() and current_track[0] != get_first_track():
        temp_list = [tracks[current_track[1] - 1], tracks[current_track[1] + 1]]
    return tuple(temp_list)


def get_first_track():
    return tracks[0]


def get_last_track():
    return tracks[-1]


def get_track_data():
    pass
