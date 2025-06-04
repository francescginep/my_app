from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid

from app import crud, schemas
from .sessions import get_db

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[schemas.ProductOut])
def read_products(store_id: uuid.UUID, db: Session = Depends(get_db)):
    products = crud.get_products_by_store(db, store_id=store_id)
    return products


@router.post("/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    store = crud.get_store(db, product.store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return crud.create_product(db, product)
