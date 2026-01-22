from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import crud
import schemas


#Create tables

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")