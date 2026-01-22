from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
import crud
import schemas


#Create tables

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# Endpoint POST
@app.post("/users", response_model=schemas.UserResponse)

def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    created_user = crud.create_user(
        db,
        username=user.username,
        email=user.email,
        password_hash=user.password
    )

    if not created_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    return created_user

# Endpoint GET
@app.get("/users", response_model=list)