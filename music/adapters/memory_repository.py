import csv
from pathlib import Path
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository, RepositoryException
from music.domainmodel.model import *


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__albums = list()
        self.__artists = list()
        self.__tracks = list()
        self.__tracks_index = dict()
        self.__users = list()
        self.__reviews = list()
        self.__playlists = list()

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


def populate(data_path: Path, repo: MemoryRepository):
    print("populate!")
    # Load articles and tags into the repository.
    #load_articles_and_tags(data_path, repo)

    # Load users into the repository.
    #users = load_users(data_path, repo)

    # Load comments into the repository.
    #load_comments(data_path, repo, users)