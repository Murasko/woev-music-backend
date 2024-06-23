from fastapi import APIRouter, Depends

from src.models.pydantic_models.song_models import Song
from src.services.auth_service import oauth2_scheme
from src.services.voting_service import get_queue, add_vote, add_song, remove_song

voting_router = APIRouter()


@voting_router.get("/queue")
async def get_local_queue():
    return get_queue()


@voting_router.post("/queue")
async def post_local_queue(song_details: Song):
    return add_song(song_details.id, song_details.song_name, song_details.artists, song_details.album_cover)


@voting_router.delete("/queue/{song_id}")
async def delete_local_queue(song_id: str, token: str = Depends(oauth2_scheme)):
    return remove_song(song_id)


@voting_router.post("/vote/{song_id}")
async def post_local_vote(song_id: str):
    return add_vote(song_id)
