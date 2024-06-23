from fastapi import Depends, FastAPI

from src.services.auth_service import oauth2_scheme
from src.routers.spotify_routes import quickplay_router, playback_router
from src.routers.auth_routes import auth_router
from src.routers.voting_routes import voting_router

app = FastAPI()

app.include_router(
    playback_router, prefix="/v1/spotify/playback", tags=["spotify-playback"],)
app.include_router(quickplay_router, prefix="/v1/spotify/quickplay",
                   tags=["spotify-quickplay"], dependencies=[Depends(oauth2_scheme)],)
app.include_router(auth_router, prefix="/v1/auth", tags=["auth"])
app.include_router(voting_router, prefix="/v1/voting", tags=["voting"])
