from typing import Annotated

from fastapi import Depends, FastAPI

from src.services.auth_service import oauth2_scheme
from src.routers import spotify_routes
from src.routers.auth_routes import auth_router

app = FastAPI()

app.include_router(
    spotify_routes.playback_router,
    prefix="/v1/spotify/playback",
    tags=["spotify-playback"],
)
app.include_router(
    spotify_routes.quickplay_router,
    prefix="/v1/spotify/quickplay",
    tags=["spotify-quickplay"],
)
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])


@app.get("/voting")
async def voting():
    return {"message": "Voting"}


@app.get("/settings")
async def settings(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
