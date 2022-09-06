# todo make this an object with attributes containing varius sorted lists and convert the methods to sort to sorted
#
from music.domainmodel.track import Track
from music.adapters.csvdatareader import TrackCSVReader
from multipledispatch import dispatch


#
# INITIALIZE a csv reader object and make it read tracks. This is needed to find the tracks needed to display them
#
#
#
# test code
# reader_obj = TrackCSVReader('tests/data/raw_albums_test.csv', 'tests/data/raw_tracks_test.csv')
#
# real deal code
def create_some_track():
    some_track = Track(1, "Heat Wavesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaas")
    some_track.track_duration = 250
    some_track.track_url = 'https://spotify/track/1'
    return some_track


class csvreader_track_methods_extension:
    def __init__(self):
        reader_obj = TrackCSVReader('tests/data/raw_albums_excerpt.csv', 'tests/data/raw_tracks_excerpt.csv')

        reader_obj.read_csv_files()
        self.__tracks = reader_obj.dataset_of_tracks

    @property
    def tracks(self):
        return self.__tracks

    def find_track(self, track_id):
        for i in self.tracks:
            if i.track_id == track_id:
                return i, self.tracks.index(i)

    def get_next_and_previous_track(self, current_track):
        temp_list = [0, 0]
        if current_track[0] == self.get_last_track():
            print("WHAT IS WRONG. TRACK PREVIOUS", self.tracks[current_track[1] - 1])
            temp_list[0] = self.tracks[current_track[1] - 1]
        elif current_track[0] == self.get_first_track():
            print("WHAT IS WRONG. TRACK PREVIOUS", self.tracks[current_track[1] + 1])
            temp_list[1] = self.tracks[current_track[1] + 1]
        elif current_track[0] != self.get_last_track() and current_track[0] != self.get_first_track():
            temp_list = [self.tracks[current_track[1] - 1], self.tracks[current_track[1] + 1]]
        return tuple(temp_list)

    def sort_by_track_name(self, tracks_list, sort_order_bool=True):
        # temp code
        if tracks_list is None:
            tracks_list = self.tracks
        tracks_list.sort(key=lambda i: i.title.upper() if i.title else '', reverse=sort_order_bool)

    def sort_by_album_name(self, tracks_list=None, sort_order_bool=True):
        if tracks_list is None:
            tracks_list = self.tracks
        tracks_list.sort(key=lambda i: i.album.title.upper() if i.album else '', reverse=sort_order_bool)

    def sort_by_track_id(self, tracks_list=None):
        if tracks_list is None:
            tracks_list = self.tracks
        tracks_list.sort()

    def get_first_track(self, tracks_list=None):
        if tracks_list is None:
            tracks_list = self.tracks
        return tracks_list[0]

    def get_last_track(self, tracks_list=None):
        if tracks_list is None:
            tracks_list = self.tracks
        return tracks_list[-1]

    # list type zero raw data
    def get_track_data(self, list_type=0):
        if list_type == 0:
            return self.tracks

    @dispatch(int)
    def create_bookmarks(self, by_track_name):
        bookmarks = None
        # the bookmarks are to allow browsing at a bookmark via link, 0= track name 1= album name 2= artist name??
        if by_track_name == 0:
            bookmarks = dict()
            for i in range(len(self.tracks)):
                if self.tracks[i].title is None and 'unnamed' not in bookmarks:
                    bookmarks['unnamed'] = self.tracks[i].track_id
                else:
                    if self.tracks[i].title[0].upper() not in bookmarks:
                        bookmarks[self.tracks[i].title[0].upper()] = self.tracks[i].track_id
                    else:
                        pass
        try:
            return bookmarks.items()
        except AttributeError:
            return None
