import csv
from pathlib import Path
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.model import *
from music.adapters.csvdatareader import TrackCSVReader

class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__albums = list()
        self.__artists = list()
        self.__tracks = list()
        self.__tracks_index = dict()
        self.__users = list()
        self.__reviews = list()
        self.__playlists = list()
        self.__genres = list()

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_track(self, track: Track):
        insort_left(self.__tracks, track)
        self.__tracks_index[track.track_id] = track

    def get_track(self, id: int) -> Track:
        track = None
        try:
            track = self.__tracks_index[id]
        except KeyError:
            pass
        return track

    def get_number_of_tracks(self) -> int:
        return len(self.__tracks)

    def get_first_track(self) -> Track:
        track = None

        if len(self.__tracks) > 0:
            track = self.__tracks[-1]
        return track

    def get_last_track(self) -> Track:
        track = None

        if len(self.__tracks) > 0:
            track = self.__tracks[-1]
        return track

    ## Get genres
    def get_genres(self) -> List[Genre]:
        genres = list()
        for track in self.__tracks:
            for genre in track.genres:
                if genre not in genres:
                    genres.append(genre)
        print("Genres = ", genres)
        return genres
    
    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

def read_csv_file(filename: str):
    with open(filename) as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row

def load_tracks(data_path: Path, repo: MemoryRepository):
    genres = dict()

    track_reader = TrackCSVReader(albums_csv_file='tests/data/raw_albums_excerpt.csv',
                 tracks_csv_file='tests/data/raw_tracks_excerpt.csv')
    print(track_reader.dataset_of_tracks)

    
    # for data_row in read_csv_file(track_filename):

    #     article_key = int(data_row[0])
    #     number_of_tags = len(data_row) - 6
    #     article_tags = data_row[-number_of_tags:]

    #     # Add any new tags; associate the current article with tags.
    #     for tag in article_tags:
    #         if tag not in genres.keys():
    #             genres[tag] = list()
    #         genres[tag].append(article_key)
    #     del data_row[-number_of_tags:]

    #     # Create Track object.
    #     track = Track(
    #         track_id=int(data_row[0]),
    #         track_title=data_row[1],
    #     )
    #     repo.add_track(track)

    # # Create Genre objects, associate them with Tracks and add them to the repository.
    # for genre_name in genres.keys():
    #     print(genres.keys)
    #     for track_id in genres[genre_name]:
    #         print(track_id)
    #         genre = Genre(genre_name)
    #         track = repo.get_track(track_id)
    #         track.add_genre(genre)
    #     repo.add_genre(genre)

def populate(data_path: Path, repo: MemoryRepository):
    print("populated!")

    # Load music and tags into the repository
    load_tracks(data_path, repo)