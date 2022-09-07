from music.domainmodel.track import Track
from music.tracks_bp.track_methods import csvreader_track_methods_extension


def album_name(track: Track):
    if track.album is not None:
        return track.album.title
    else:
        return None


def artist_name(track: Track):
    if track.artist is not None:
        return track.artist.full_name
    else:
        return None


def track_obj_to_dict(track: Track):
    return {
        'track_id': track.track_id,
        'track_name': track.title,
        'duration': track.track_duration,
        'url': track.track_url,
        'album': album_name(track),
        'artist': artist_name(track)
    }
