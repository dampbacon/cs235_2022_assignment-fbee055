from datetime import date, datetime
from typing import List

import pytest

from music.adapters.repository import RepositoryException
from music.domainmodel.model import Album, Artist, Genre, Track, PlayList, Review, User

def test_repository_can_add_a_track(in_memory_repo):
    track = Track(1000, "Test Track")
    in_memory_repo.add_track(track)

    assert in_memory_repo.get_track(1000) is track

def test_repository_can_retrieve_a_track(in_memory_repo):
    track = in_memory_repo.get_track(2)

    assert track.title == "Food"

def test_repository_does_not_retrieve_a_non_existent_track(in_memory_repo):
    track = in_memory_repo.get_track(999999)

    assert track is None

def test_repository_can_retrieve_track_count(in_memory_repo):
    number_of_tracks = in_memory_repo.get_number_of_tracks()

    # Check that the query returned 2000 Tracks.
    assert number_of_tracks == 2000

# def test_repository_can_add_a_user(in_memory_repo):
#     user = User(100, "Test User", "123456789")
#     in_memory_repo.add_user(user)

#     assert in_memory_repo.get_user("Test User") is user

# def test_repository_can_retrieve_a_user(in_memory_repo):
#     user = in_memory_repo.get_user("thorke")

#     assert user.user_name == "thorke"
#     assert user.password == "123456789"

def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user("fakeuser123")

    assert user is None

def test_repository_can_retrieve_user_count(in_memory_repo):
    number_of_users = in_memory_repo.get_number_of_users()

    assert number_of_users == 0

def test_repository_can_retrieve_first_track(in_memory_repo):
    track = in_memory_repo.get_first_track()

    assert track.title == "Food"

def test_repository_can_retrieve_last_track(in_memory_repo):
    track = in_memory_repo.get_last_track()

    assert track.title == "yet to be titled"

def test_repository_can_get_track_by_id(in_memory_repo):
    tracks = in_memory_repo.get_tracks_by_id([2, 5])

    assert len(tracks) == 2

    track_ids = [track.track_id for track in tracks]

    assert 2 in track_ids
    assert 5 in track_ids

def test_repository_does_not_retrieve_a_non_existent_track_when_searching_by_id(in_memory_repo):
    tracks = in_memory_repo.get_tracks_by_id([2, 1000])

    assert len(tracks) == 2

    track_ids = [track.track_id for track in tracks]

    assert 2 in track_ids
    assert 1001 not in track_ids

def test_repository_get_genre_returns_genre(in_memory_repo):
    genres = in_memory_repo.get_genres()
    print(genres)
    assert genres

def test_repository_get_genre_returns_empty_list_for_non_existent_genre(in_memory_repo):
    genres = in_memory_repo.get_genres()
    assert genres

# def test_repository_add_genre(in_memory_repo):
#     genre = Genre(1, "Test Genre")
#     in_memory_repo.add_genre(genre)

#     assert in_memory_repo.get_genre("Test Genre") is genre

def test_repository_can_retrieve_genre_count(in_memory_repo):
    number_of_genres = in_memory_repo.get_number_of_genres()

    assert number_of_genres == 60


## Album, artist, playlist

def test_album_can_be_constructed():
    album = Album(1, "Test Album")
    assert album.album_id == 1
    assert album.title == "Test Album"
    assert repr(album) == "<Album Test Album, album id = 1>"

def test_album_can_be_compared():
    album1 = Album(1, "Test Album")
    album2 = Album(2, "Test Album")
    album3 = Album(1, "Test Album")
    assert album1 != album2
    assert album1 == album3

# artist tests
def test_artist_can_be_compared():
    artist1 = Artist(1, "Test Artist")
    artist2 = Artist(2, "Test Artist")
    artist3 = Artist(1, "Test Artist")
    assert artist1 != artist2
    assert artist1 == artist3
