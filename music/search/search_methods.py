from music.adapters.memory_repository import MemoryRepository as Test_repo

# import music.adapters.repository as repo
repo = Test_repo()
# [1,2,3,4,5,6,7,8,9,10]

def search_by_album_name(repository=repo, string_to_search='free', shallow_search=False):
    tracks_sorted_by_albums = repository.tracks_a
    bookmarks = list(repository.create_bookmarks(tracks_sorted_by_albums, 1))
    # [item,item.........]
    results_with_search_term_at_front = []
    result_with_search_term_in_middle_or_end = []
    index = None
    index_end = None
    for i in range(0, len(bookmarks)):
        if bookmarks[i][0] == string_to_search[0].upper():
            index = bookmarks[i]
            if bookmarks[i] != bookmarks[-1]:
                index_end = bookmarks[i+1]

            break
    print(index, index_end)
    realIndex1 = tracks_sorted_by_albums.index(repository.get_track(index[1]))
    realIndex2 = None
    if index_end is None:
        realIndex2 = len(tracks_sorted_by_albums)
    else:
        realIndex2 = tracks_sorted_by_albums.index(repository.get_track(index_end[1]))
    print(realIndex1,realIndex2)
    for i in range(realIndex1,realIndex2):
        #print(index, index_end)
        if tracks_sorted_by_albums[i].album is not None:
            if tracks_sorted_by_albums[i].album.title[:len(string_to_search)].upper() == string_to_search.upper():
                results_with_search_term_at_front.append(tracks_sorted_by_albums[i])
    if shallow_search==True:
        return results_with_search_term_at_front
    for i in range(0, len(tracks_sorted_by_albums)):
        if tracks_sorted_by_albums[i].album is not None:
            if string_to_search.upper() in tracks_sorted_by_albums[i].album.title.upper():
                if tracks_sorted_by_albums[i] not in results_with_search_term_at_front:
                    result_with_search_term_in_middle_or_end.append(tracks_sorted_by_albums[i])
    return results_with_search_term_at_front, result_with_search_term_in_middle_or_end


def search_by_track_name(repository=repo, string_to_search='free', shallow_search=False):
    tracks_by_track_name = repository.tracks_t
    bookmarks = list(repository.create_bookmarks(tracks_by_track_name, 0))
    # [item,item.........]
    results_with_search_term_at_front = []
    result_with_search_term_in_middle_or_end = []
    index = None
    index_end = None
    for i in range(0, len(bookmarks)):
        if bookmarks[i][0] == string_to_search[0].upper():
            index = bookmarks[i]
            if bookmarks[i] != bookmarks[-1]:
                index_end = bookmarks[i+1]

            break
    print(index, index_end)
    realIndex1 = tracks_by_track_name.index(repository.get_track(index[1]))
    realIndex2 = None
    if index_end is None:
        realIndex2 = len(tracks_by_track_name)
    else:
        realIndex2 = tracks_by_track_name.index(repository.get_track(index_end[1]))
    print(realIndex1,realIndex2)
    for i in range(realIndex1,realIndex2):
        #print(index, index_end)
        if tracks_by_track_name[i].title is not None:
            if tracks_by_track_name[i].title[:len(string_to_search)].upper() == string_to_search.upper():
                results_with_search_term_at_front.append(tracks_by_track_name[i])
    if shallow_search==True:
        return results_with_search_term_at_front
    for i in range(0, len(tracks_by_track_name)):
        if tracks_by_track_name[i].title is not None:
            if string_to_search.upper() in tracks_by_track_name[i].title.upper():
                if tracks_by_track_name[i] not in results_with_search_term_at_front:
                    result_with_search_term_in_middle_or_end.append(tracks_by_track_name[i])
    return results_with_search_term_at_front, result_with_search_term_in_middle_or_end


def search_by_artist_name(repository=repo, string_to_search='free', shallow_search=False):
    tracks_by_artist_name = repository.tracks_artist
    bookmarks = list(repository.create_bookmarks(tracks_by_artist_name, 1))
    # [item,item.........]
    results_with_search_term_at_front = []
    result_with_search_term_in_middle_or_end = []
    index = None
    index_end = None
    for i in range(0, len(bookmarks)):
        if bookmarks[i][0] == string_to_search[0].upper():
            index = bookmarks[i]
            if bookmarks[i] != bookmarks[-1]:
                index_end = bookmarks[i+1]

            break
    print(index, index_end)
    realIndex1 = tracks_by_artist_name.index(repository.get_track(index[1]))
    realIndex2 = None
    if index_end is None:
        realIndex2 = len(tracks_by_artist_name)
    else:
        realIndex2 = tracks_by_artist_name.index(repository.get_track(index_end[1]))
    print(realIndex1,realIndex2)
    for i in range(realIndex1,realIndex2):
        #print(index, index_end)
        if tracks_by_artist_name[i].artist is not None:
            if tracks_by_artist_name[i].artist.full_name[:len(string_to_search)].upper() == string_to_search.upper():
                results_with_search_term_at_front.append(tracks_by_artist_name[i])
    if shallow_search==True:
        return results_with_search_term_at_front
    for i in range(0, len(tracks_by_artist_name)):
        if tracks_by_artist_name[i].artist is not None:
            if string_to_search.upper() in tracks_by_artist_name[i].artist.full_name.upper():
                if tracks_by_artist_name[i] not in results_with_search_term_at_front:
                    result_with_search_term_in_middle_or_end.append(tracks_by_artist_name[i])
    for i in results_with_search_term_at_front:
        print(i.artist.full_name)

    for i in result_with_search_term_in_middle_or_end:
        print(i.artist.full_name)
    return results_with_search_term_at_front, result_with_search_term_in_middle_or_end



