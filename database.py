from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

uri = os.environ.get("MYSQL_URI")
username = os.environ.get("MYSQL_USERNAME")
password = os.environ.get("MYSQL_PASSWORD")
db_name = os.environ.get("DATABASE_NAME")

con_string = f"mysql+pymysql://{username}:{password}@{uri}/{db_name}"

# SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"
SQLALCHEMY_DATABASE_URL = con_string

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
