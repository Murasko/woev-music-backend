import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv

load_dotenv()

scope = (
    "user-read-recently-played,"
    "streaming,"
    "user-library-read,"
    "user-read-currently-playing,"
    "user-modify-playback-state,"
    "user-read-playback-state"
)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def next_song():
    sp.next_track()
    return {"message": "Next Song"}


def previous_song():
    sp.previous_track()
    return {"message": "Previous Song"}


def change_playback():
    current_playback = sp.current_playback()
    if not current_playback:
        return {"message": "No playback found"}
    if current_playback["is_playing"]:
        sp.pause_playback()
        return {"message": "Paused playback"}
    else:
        sp.start_playback()
        return {"message": "Started playback"}


def shuffle():
    current_playback = sp.current_playback()
    if not current_playback:
        return {"message": "No playback found"}

    if current_playback["shuffle_state"]:
        sp.shuffle(state=False)
        return {"message": "Shuffle deactivated"}
    else:
        sp.shuffle(state=True)
        return {"message": "Shuffle activated"}


def woev_playlist():
    sp.shuffle(state=True)
    sp.start_playback(context_uri="spotify:playlist:6uj2V0i1h2yEO8TDYcdtUc")
    return {"message": "Playing Woev Playlist"}


def trinkgut():
    sp.repeat(state="Track")
    sp.start_playback(
        uris=[
            "spotify:track:1dwTG4PVhiWzeu0fUfMMMb",
        ]
    )
    return {"message": "Playing Trinkgut Playlist"}


def search(query: str):
    search_results = sp.search(q=query, limit=50)
    if not search_results:
        return {"message": "No results found"}
    else:
        songs = []
        for track in search_results["tracks"]["items"]:
            track_artists = []
            song_name = track["name"]
            for artist in track["artists"]:
                track_artists.append(artist["name"])
            songs.append(
                {
                    "song_name": song_name,
                    "artists": ", ".join(track_artists),
                    "song_id": track["id"],
                    "album_cover": track["album"]["images"][0]["url"],
                }
            )
    return songs


def queue_add(song_id: str):
    if not song_id:
        return {"message": "No song id provided"}
    else:
        sp.add_to_queue(song_id)
        return {"message": "Added Song to queue"}


def get_queue():
    queue = sp.queue()
    if not queue:
        return {"message": "No results found"}
    else:
        queue_songs = []
        for track in queue["queue"]:
            track_artists = []
            song_name = track["name"]
            for artist in track["artists"]:
                track_artists.append(artist["name"])
            queue_songs.append(
                {
                    "song_name": song_name,
                    "artists": ", ".join(track_artists),
                    "album_cover": track["album"]["images"][0]["url"],
                }
            )
    return queue_songs


def get_current_song():
    current_song = sp.currently_playing()
    if not current_song:
        return {"message": "No playback found"}
    else:
        track = current_song["item"]
        track_artists = []
        song_name = track["name"]
        for artist in track["artists"]:
            track_artists.append(artist["name"])
        return {
            "song_name": song_name,
            "artists": ", ".join(track_artists),
            "album_cover": track["album"]["images"][0]["url"],
        }
