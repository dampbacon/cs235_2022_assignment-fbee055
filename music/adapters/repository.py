import abc
from typing import List
from datetime import date

from music.domainmodel.model import *

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name) -> User:
        """ Returns the User named user_name from the repository.

        If there is no User with the given user_name, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_track(self, track: Track):
        """ Adds an Track to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_track(self, id: int) -> Track:
        """ Returns Track with id from the repository.

        If there is no Track with the given id, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_tracks(self) -> int:
        """ Returns the number of Tracks in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_track(self) -> Track:
        """ Returns the first Track from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_track(self) -> Track:
        """ Returns the last Track from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the list of genres in the repository. """
        raise NotImplementedError
