from fastapi import APIRouter

import src.services.spotify_service as spotify

playback_router = APIRouter()
quickplay_router = APIRouter()


@playback_router.get("/")
async def current_song():
    playback = spotify.get_current_song()
    return playback


@playback_router.post("/next")
async def next_song():
    response = spotify.next_song()
    return response


@playback_router.post("/previous")
async def previous_song():
    response = spotify.previous_song()
    return response


@playback_router.post("/play-pause")
async def play_pause():
    response = spotify.change_playback()
    return response


@playback_router.post("/shuffle")
async def shuffle():
    response = spotify.shuffle()
    return response


@quickplay_router.post("/woev-playlist")
async def woev_playlist():
    response = spotify.woev_playlist()
    return response


@quickplay_router.post("/trinkgut")
async def trinkgut():
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
