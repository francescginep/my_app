from urllib import request
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from ..database import SessionLocal
from .. import models
from uuid import UUID

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sessions/start")
def start_session(user_id: UUID, store_id: UUID, db: Session = Depends(get_db)):
    new_session = crud.create_session(db, user_id, store_id)
    return {"session_id": new_session.id}
