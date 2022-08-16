from datetime import date, datetime, timedelta
from statistics import mode
from sqlalchemy.orm import Session
from sqlalchemy import desc, or_
import datetime as DT

from models import models

from schemas import schemas

def get_actor(db: Session, actor_id: int):
    return db.query(models.Actors).filter(models.Actors.id == actor_id).first()


def get_actor_by_firstname(db: Session, firstname: str):
    return db.query(models.Actors).filter(models.Actors.firstname == firstname).all()


def get_actors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Actors).offset(skip).limit(limit).all()


def create_actor(db: Session, actor: schemas.ActorCreate):
    db_user = models.Actors(firstname=actor.firstname,
                            lastname=actor.lastname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movies).offset(skip).limit(limit).all()


def get_all_movies(db: Session):
    return db.query(models.Movies).all()


def get_all_movies_by_date(db: Session):
    return db.query(models.Movies).order_by(desc(models.Movies.release_date)).all()


def get_latest_movies(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Movies).order_by(desc(models.Movies.release_date)).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_user = models.Movies(title=movie.title,
                            release_date=movie.release_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


##### ######
# def get_movies_by_category(db: Session, category: int):
#     return db.query(models.models).filter(models.Movies.category == category).all()
