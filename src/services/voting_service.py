from src.models.db_models.song_queue import Song, Session


def get_queue():
    session = Session()
    songs = session.query(Song).all()
    session.close()
    return {"songs": [{"song_id": song.song_id, "title": song.title, "artists": song.artists, "album_cover": song.album_cover, "votes": song.votes} for song in songs]}


def add_vote(song_id: str):
    session = Session()
    song = session.query(Song).filter_by(song_id=song_id).first()
    if song:
        song.votes += 1
        session.commit()
        message = "Vote added"
    else:
        message = "Song not found"
    session.close()
    return {"message": message}


def add_song(song_id: str, title: str, artists: str, album_cover: str):
    session = Session()
    if not session.query(Song).filter_by(song_id=song_id).first():
        new_song = Song(song_id=song_id, title=title,
                        artists=artists, album_cover=album_cover)
        session.add(new_song)
        session.commit()
        message = "Song added"
    else:
        add_vote(song_id)
    session.close()
    return {"message": message}


def remove_song(song_id: str):
    session = Session()
    song = session.query(Song).filter_by(song_id=song_id).first()
    if song:
        session.delete(song)
        session.commit()
        message = "Song removed"
    else:
        message = "Song not found"
    session.close()
    return {"message": message}
