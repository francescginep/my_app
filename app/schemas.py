from pydantic import BaseModel, UUID4
from typing import Optional, List
from datetime import datetime


class AddToCartRequest(BaseModel):
    session_id: str
    barcode: str

# ---------- User ----------
class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: UUID4


# ---------- Store ----------
class StoreBase(BaseModel):
    name: str

class StoreCreate(StoreBase):
    pass

class StoreOut(StoreBase):
    id: UUID4


# ---------- Product ----------
class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    store_id: UUID4

class ProductOut(ProductBase):
    id: UUID4
    store_id: UUID4


# ---------- CartItem ----------
class CartItemBase(BaseModel):
    quantity: float = 1

class CartItemCreate(CartItemBase):
    product_id: UUID4
    user_id: UUID4

class CartItemOut(CartItemBase):
    id: UUID4
    product_id: UUID4
    user_id: UUID4


# ---------- Payment ----------
class PaymentBase(BaseModel):
    amount: float
    success: Optional[bool] = True

class PaymentCreate(PaymentBase):
    user_id: UUID4

class PaymentOut(PaymentBase):
    id: UUID4
    user_id: UUID4
    timestamp: datetime
