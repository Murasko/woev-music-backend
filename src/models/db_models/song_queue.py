from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db/postgres"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Song(Base):
    __tablename__ = 'songs'

    song_id = Column(String, primary_key=True)
    title = Column(String)
    artists = Column(String)
    album_cover = Column(String)
    votes = Column(Integer, default=1)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
