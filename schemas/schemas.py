from datetime import datetime
from email import message
from lib2to3.pgen2 import token
from typing import List, Optional
from unicodedata import category

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    release_date: Optional[datetime]


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class ActorBase(BaseModel):
    firstname: str
    lastname: str


class ActorCreate(ActorBase):
    pass


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True


class MovieActorBase(BaseModel):
    movie_id: int
    actor_id: int


class MovieActorCreate(MovieActorBase):
    pass


class MovieActor(MovieActorBase):
    id: int

    class Config:
        orm_mode = True
