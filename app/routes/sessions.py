from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
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
    new_session = models.Session(user_id=user_id, store_id=store_id)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return {"session_id": new_session.id}
