from fastapi import FastAPI

from src.routers import spotify

app = FastAPI()

app.include_router(spotify.router, prefix="/v1/spotify", tags=["spotify"])
app.include_router(spotify.playback_router, prefix="/v1/spotify/playback", tags=["spotify-playback"])
app.include_router(spotify.quickplay_router, prefix="/v1/spotify/quickplay", tags=["spotify-quickplay"])

@app.get("/voting")
async def voting():
    return {"message": "Voting"}

@app.get("/settings")
async def settings():
    return {"message": "Settings"}
