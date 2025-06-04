from sqlalchemy.orm import Session
from . import models, schemas
import uuid
from datetime import datetime

def create_session(db: Session, user_id: uuid.UUID, store_id: uuid.UUID):
    new_session = models.Session(
        id=uuid.uuid4(),
        user_id=user_id,
        store_id=store_id,
        start_time=datetime.utcnow()
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session
# ---- USERS ----
def get_user(db: Session, user_id: uuid.UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(id=uuid.uuid4(), name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ---- STORES ----
def get_store(db: Session, store_id: uuid.UUID):
    return db.query(models.Store).filter(models.Store.id == store_id).first()

def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(id=uuid.uuid4(), name=store.name)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store


# ---- PRODUCTS ----
def get_product(db: Session, product_id: uuid.UUID):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products_by_store(db: Session, store_id: uuid.UUID):
    return db.query(models.Product).filter(models.Product.store_id == store_id).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        id=uuid.uuid4(),
        name=product.name,
        price=product.price,
        store_id=product.store_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# ---- CART ITEMS ----
def get_cart_items_by_user(db: Session, user_id: uuid.UUID):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()

def add_cart_item(db: Session, cart_item: schemas.CartItemCreate):
    db_item = models.CartItem(
        id=uuid.uuid4(),
        user_id=cart_item.user_id,
        product_id=cart_item.product_id,
        quantity=cart_item.quantity,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def remove_cart_item(db: Session, cart_item_id: uuid.UUID):
    item = db.query(models.CartItem).filter(models.CartItem.id == cart_item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item


# ---- PAYMENTS ----
def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(
        id=uuid.uuid4(),
        user_id=payment.user_id,
        amount=payment.amount,
        success=payment.success if payment.success is not None else True,
        timestamp=datetime.utcnow(),
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payments_by_user(db: Session, user_id: uuid.UUID):
    return db.query(models.Payment).filter(models.Payment.user_id == user_id).all()
