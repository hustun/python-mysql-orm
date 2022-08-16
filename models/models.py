from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class MovieActor(Base):
    __tablename__ = "movie_actor"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))


class Actors(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100), index=True)
    lastname = Column(String(100), index=True)


class Movies(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    release_date = Column(DateTime)
