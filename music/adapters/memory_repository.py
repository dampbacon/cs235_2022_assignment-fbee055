import csv
from pathlib import Path
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

import multipledispatch
from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.model import *
from music.adapters.csvdatareader import TrackCSVReader


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__users = list()
        self.__reviews = list()
        self.__playlists = list()

        # default
        self.__csv_reader = TrackCSVReader(albums_csv_file='tests/data/raw_albums_excerpt.csv',
                                           tracks_csv_file='tests/data/raw_tracks_excerpt.csv')

        self.__csv_reader.read_csv_files()
        self.__albums = self.__csv_reader.dataset_of_albums
        self.__artists = self.__csv_reader.dataset_of_artists
        self.__genres = self.__csv_reader.dataset_of_genres
        self.__tracks = self.__csv_reader.dataset_of_tracks
        self.__tracks_sbt = self.sort_by_track_name(self.__tracks, False)
        self.__tracks_sba = self.sort_by_album_name(self.__tracks, False)
        self.__tracks_sb_artist = self.sort_by_artist_name(self.__tracks, False)
        self.__tracks_genre = self.sort_by_genre(self.__tracks, False)

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def csv_reader_read(self):
        self.__csv_reader.read_csv_files()

    def csv_reader_new_files(self, albums: str, tracks: str):
        self.__csv_reader = None
        self.__csv_reader = TrackCSVReader(albums, tracks)
        self.csv_reader_read()
        self.__genres = self.__csv_reader.dataset_of_genres
        self.__tracks = self.__csv_reader.dataset_of_tracks
        self.__artists = self.__csv_reader.dataset_of_artists
        self.__albums = self.__csv_reader.dataset_of_albums
        self.refresh_lists()

    @property
    def genres(self):
        return self.__genres

    @property
    def tracks(self):
        return self.__tracks

    @property
    def artists(self):
        return self.__artists

    @property
    def albums(self):
        return self.__albums


    @property
    def tracks_a(self):
        return self.__tracks_sba

    @property
    def tracks_t(self):
        return self.__tracks_sbt

    @property
    def tracks_artist(self):
        return self.__tracks_sb_artist

    def refresh_lists(self):
        self.__tracks_sba = self.sort_by_album_name(self.tracks)
        self.__tracks_sbt = self.sort_by_track_name(self.tracks)
        self.__tracks_sb_artist = self.sort_by_artist_name(self.tracks)
        self.__tracks_genre = self.sort_by_genre(self.tracks)

    def add_track(self, track: Track):
        insort_left(self.__tracks, track)
        self.refresh_lists()

    def get_track(self, id: int) -> Track:
        tracks_list = self.tracks
        for i in tracks_list:
            if i.track_id == id:
                return i

    def find_track(self, tracks_list, track_id):
        if tracks_list is None:
            tracks_list = self.tracks
        for i in tracks_list:
            if i.track_id == track_id:
                return i, tracks_list.index(i)

    def get_number_of_tracks(self) -> int:
        return len(self.__tracks)

    def get_last_track(self, tracks_list=None) -> Track:
        track = None
        if tracks_list is None:
            tracks_list = self.tracks
        if len(tracks_list) > 0:
            track = tracks_list[-1]
        return track

    def get_first_track(self, tracks_list=None):
        track = None
        if tracks_list is None:
            tracks_list = self.tracks
        if len(tracks_list) > 0:
            track = tracks_list[0]
        return track

    ## Get genres
    def get_genres(self) -> set[Genre]:
        return self.genres

    def add_genre(self, genre: Genre):
        self.__genres.add(genre)

    def sort_by_track_name(self, tracks_list, sort_order_bool=True):
        # temp code
        if tracks_list is None:
            tracks_list = self.tracks
        return sorted(tracks_list, key=lambda i: i.title.upper() if i.title else '', reverse=sort_order_bool)

    def sort_by_album_name(self, tracks_list=None, sort_order_bool=True):
        if tracks_list is None:
            tracks_list = self.tracks
        return sorted(tracks_list, key=lambda i: i.album.title.upper() if i.album else '', reverse=sort_order_bool)

    def sort_by_artist_name(self, tracks_list=None, sort_order_bool=True):
        if tracks_list is None:
            tracks_list = self.tracks
        return sorted(tracks_list, key=lambda i: i.artist.full_name.upper() if i.artist else '',
                      reverse=sort_order_bool)

    def sort_by_track_id(self, tracks_list=None):
        if tracks_list is None:
            tracks_list = self.tracks
        return sorted(tracks_list)

    def sort_by_genre(self, tracks_list=None, sort_order_bool=True):
        if tracks_list is None:
            tracks_list = self.tracks
        return sorted(tracks_list, key=lambda i: str(i.genres[0]).upper() if i.genres else '', reverse=sort_order_bool)

    def get_next_and_previous_track(self, tracks_list, current_track):
        if tracks_list is None:
            tracks_list = tracks_list
        temp_list = [0, 0]
        if current_track[0] == self.get_last_track(tracks_list):
            # print("WHAT IS WRONG. TRACK PREVIOUS", tracks_list[current_track[1] - 1])
            temp_list[0] = tracks_list[current_track[1] - 1]
        elif current_track[0] == self.get_first_track(tracks_list):
            # print("WHAT IS WRONG. TRACK PREVIOUS", tracks_list[current_track[1] + 1])
            temp_list[1] = tracks_list[current_track[1] + 1]
        elif current_track[0] != self.get_last_track(tracks_list) \
                and current_track[0] != self.get_first_track(tracks_list):
            temp_list = [tracks_list[current_track[1] - 1], tracks_list[current_track[1] + 1]]
        return tuple(temp_list)

    def create_bookmarks(self, tracks_list, by_track_name):
        if tracks_list is None:
            tracks_list = self.tracks
        bookmarks = None
        # the bookmarks are to allow browsing at a bookmark via link, 0= track name 1= album name 2= artist name??
        if by_track_name == 0:
            bookmarks = dict()
            for i in range(len(tracks_list)):
                if tracks_list[i].title is None and 'unnamed' not in bookmarks:
                    bookmarks['unnamed'] = tracks_list[i].track_id
                else:
                    if tracks_list[i].title[0].upper() not in bookmarks:
                        bookmarks[tracks_list[i].title[0].upper()] = tracks_list[i].track_id
                    else:
                        pass
        elif by_track_name == 1:
            bookmarks = dict()
            for i in range(len(tracks_list)):
                if tracks_list[i].album:
                    if tracks_list[i].album.title is None and 'No album' not in bookmarks:
                        bookmarks['No album'] = tracks_list[i].track_id
                    else:
                        if tracks_list[i].album.title[0].upper() not in bookmarks:
                            bookmarks[tracks_list[i].album.title[0].upper()] = tracks_list[i].track_id
                        else:
                            pass
                else:
                    if 'No album' not in bookmarks:
                        bookmarks['No album'] = tracks_list[i].track_id

            pass
        elif by_track_name == 2:
            bookmarks = dict()
            for i in range(len(tracks_list)):
                if tracks_list[i].artist:
                    if tracks_list[i].artist.full_name is None and 'No name' not in bookmarks:
                        bookmarks['No name'] = tracks_list[i].track_id
                    else:
                        if tracks_list[i].artist.full_name[0].upper() not in bookmarks:
                            bookmarks[tracks_list[i].artist.full_name[0].upper()] = tracks_list[i].track_id
                        else:
                            pass
                else:
                    if 'No name' not in bookmarks:
                        bookmarks['No name'] = tracks_list[i].track_id
        try:
            return bookmarks.items()
        except AttributeError:
            return None


# todo idk why this exists when we are given class csv reader with in build reader (csvdatareader)
# def read_csv_file(filename: str):
#     with open(filename) as infile:
#         reader = csv.reader(infile)
#         # Read first line of the the CSV file.
#         headers = next(reader)
#         # Read remaining rows from the CSV file.
#         for row in reader:
#             # Strip any leading/trailing white space from data read.
#             row = [item.strip() for item in row]
#             yield row

# todo idk why this exists also genres albums and other stuff are properties of the reader
def load_tracks(data_path: Path, repo: MemoryRepository):
    genres = dict()

    repo.csv_reader_new_files('tests/data/raw_albums_excerpt.csv',
                              'tests/data/raw_tracks_excerpt.csv')

    print(repo.tracks)
    print("TEST")


    # track_reader = TrackCSVReader(albums_csv_file='tests/data/raw_albums_excerpt.csv',
    #                               tracks_csv_file='tests/data/raw_tracks_excerpt.csv')


#     # for data_row in read_csv_file(track_filename):
#
#     #     article_key = int(data_row[0])
#     #     number_of_tags = len(data_row) - 6
#     #     article_tags = data_row[-number_of_tags:]
#
#     #     # Add any new tags; associate the current article with tags.
#     #     for tag in article_tags:
#     #         if tag not in genres.keys():
#     #             genres[tag] = list()
#     #         genres[tag].append(article_key)
#     #     del data_row[-number_of_tags:]
#
#     #     # Create Track object.
#     #     track = Track(
#     #         track_id=int(data_row[0]),
#     #         track_title=data_row[1],
#     #     )
#     #     repo.add_track(track)
#
#     # # Create Genre objects, associate them with Tracks and add them to the repository.
#     # for genre_name in genres.keys():
#     #     print(genres.keys)
#     #     for track_id in genres[genre_name]:
#     #         print(track_id)
#     #         genre = Genre(genre_name)
#     #         track = repo.get_track(track_id)
#     #         track.add_genre(genre)
#     #     repo.add_genre(genre)
#

def populate(data_path: Path, repo: MemoryRepository):
    print("populated!")
    # Load music and tags into the repository
    load_tracks(data_path, repo)


from music.domainmodel.model import *
from music.adapters.csvdatareader import TrackCSVReader
from multipledispatch import dispatch
