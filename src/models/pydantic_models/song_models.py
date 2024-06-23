from pydantic import BaseModel


class Song(BaseModel):
    id: str
    song_name: str
    artists: str
    album_cover: str
