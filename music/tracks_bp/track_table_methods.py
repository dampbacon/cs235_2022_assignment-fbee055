from music.domainmodel.model import *
from music.tracks_bp.track_methods import csvreader_track_methods_extension


def album_name(track: Track):
    if track.album is not None:
        return track.album.title
    else:
        return 'None'


def artist_name(track: Track):
    if track.artist is not None:
        return track.artist.full_name
    else:
        return 'none'


def track_name(track: Track):
    if track.title is not None:
        return track.title
    else:
        return 'none'


def track_duration(track: Track):
    if track.track_duration is not None:
        return track.track_duration
    else:
        return 0


def track_obj_to_dict(track: Track):
    return {
        'track_id': int(track.track_id),
        'track_name': str(track_name(track)),
        'duration': int(track_duration(track)),
        'url': '/track/' + str(track.track_id),
        'album': str(album_name(track)),
        'artist': str(artist_name(track))
    }
