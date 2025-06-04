from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..schemas import *
from .. import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cart/add")
def add_product_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    cart_item = crud.add_to_cart(db, request.session_id, request.barcode)
    if not cart_item:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto añadido al carrito"}
