from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Integer
from sqlalchemy.orm import Session
import hashlib
import jwt
import time
from datetime import datetime, timezone, timedelta
from dependency import has_access

from crud import crud

from models import models

from schemas import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# routes
# PROTECTED = [Depends(has_access)]
PROTECTED = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def root():
    return {"message": "Hello World"}

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/api/login", response_model=schemas.__)
# def login(payload: schemas.__, db: Session = Depends(get_db)):

#     db_user = get_user
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Username incorrect.")
#     if not db_user.password:
#         raise HTTPException(status_code=400, detail="Password error.")
#     hashed_pass_input = hashlib.sha256(
#         payload.password.encode('utf-8')).hexdigest()

#     if db_user.password == hashed_pass_input:
#         expire_date = datetime.now(tz=timezone.utc) + timedelta(days=10)
#         token = jwt.encode(
#             {"exp": expire_date}, "", algorithm="HS256") 

#         return {"success": True, "token": token}
#     else:
#         raise HTTPException(status_code=400, detail="Wrong password.")


@app.post("/api/actors/", response_model=schemas.Actor, dependencies=PROTECTED)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(get_db)):
    # db_actor = crud.get_actor_by_firstname(db, firstname=actor.firstname)
    # if db_actor:
    #     raise HTTPException(status_code=400, detail="Actor already exists.")
    return crud.create_actor(db=db, actor=actor)


@app.get("/api/actors/", response_model=List[schemas.Actor], dependencies=PROTECTED)
def read_actors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    actors = crud.get_actors(db, skip=skip, limit=limit)
    return actors


@app.get("/api/actors/{actor_id}", response_model=schemas.Actor, dependencies=PROTECTED)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    print(actor_id)
    actor = crud.get_actor(db, actor_id == actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@app.get("/api/movies/", response_model=List[schemas.Movie], dependencies=PROTECTED)
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_movies(db, skip=skip, limit=limit)
    return items


@app.post("/api/movies/", response_model=schemas.Movie, dependencies=PROTECTED)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    # db_movie = crud.get_movie_by_title(db, title=movie.title)
    # if db_movie:
    #     raise HTTPException(status_code=400, detail="Movie already exists.")
    return crud.create_movie(db=db, movie=movie)


@app.get("/api/movies/all", response_model=List[schemas.Movie], dependencies=PROTECTED)
def read_all_movies(db: Session = Depends(get_db)):
    items = crud.get_all_movies_by_date(db)
    return items


@app.get("/api/movies/latest", response_model=List[schemas.Movie], dependencies=PROTECTED)
def read_latest_movies(skip: int = 0, limit: int = 5, db: Session = Depends(get_db)):
    items = crud.get_latest_movies(db, skip=skip, limit=limit)
    return items
