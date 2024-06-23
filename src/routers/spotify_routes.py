from fastapi import APIRouter, Depends

from src.services.auth_service import oauth2_scheme
import src.services.spotify_service as spotify

playback_router = APIRouter()
quickplay_router = APIRouter()


@playback_router.get("/")
async def current_song():
    playback = spotify.get_current_song()
    return playback


@playback_router.post("/next")
async def next_song(token: str = Depends(oauth2_scheme)):
    response = spotify.next_song()
    return response


@playback_router.post("/previous")
async def previous_song(token: str = Depends(oauth2_scheme)):
    response = spotify.previous_song()
    return response


@playback_router.post("/play-pause")
async def play_pause(token: str = Depends(oauth2_scheme)):
    response = spotify.change_playback()
    return response


@playback_router.post("/shuffle")
async def shuffle(token: str = Depends(oauth2_scheme)):
    response = spotify.shuffle()
    return response


@quickplay_router.post("/woev-playlist")
async def woev_playlist(token: str = Depends(oauth2_scheme)):
    response = spotify.woev_playlist()
    return response


@quickplay_router.post("/trinkgut")
async def trinkgut(token: str = Depends(oauth2_scheme)):
    response = spotify.trinkgut()
    return response


@playback_router.post("/search/{query}")
async def search(query: str):
    response = spotify.search(query)
    return response


@playback_router.get("/queue")
async def queue():
    response = spotify.get_queue()
    return response


@playback_router.post("/queue/{song_id}")
async def queue_add(song_id: str):
    response = spotify.queue_add(song_id)
    return response
