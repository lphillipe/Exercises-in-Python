from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import crud, schemas, security

from app.security import get_current_user
from app.models import User

from fastapi.security import OAuth2PasswordRequestForm

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="User Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Endpoint POST Create USERS
@app.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    created_user = crud.create_user(
        db,
        username=user.username,
        email=user.email,
        password=user.password
    )

    if not created_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    return created_user

# Endpoint GET List users
@app.get("/users", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

# Endpoint GET Search by ID
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return user

@app.put("/users/{user_id}/username", response_model=schemas.UserResponse)
def update_username(user_id: int, username: str, db: Session = Depends(get_db)):
    user = crud.update_user_username(db, user_id, username)

    if not user:
        raise HTTPException(status_code=400, detail="Not possible to update")

    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted = crud.delete_user_by_id(db, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(
        db,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    token = security.create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }