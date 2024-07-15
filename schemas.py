from typing_extensions import Self
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, Any


class SignUp(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool = True
    is_staff: bool = False


class LoginModel(BaseModel):
    username_or_email: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = "24084df22271e59fa98e57a3ae3cf18315e80c8dbb5748b8792ce4db86f73f69"


class OrderModel(BaseModel):
    id: Optional[int]
    quanty: int
    user_id: Optional[int]
    product_id: Optional[int]
    order_status: Optional[str] = "PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
                "example": {
                    "quanty": 1,
                }
            }


class OrderStatus(BaseModel):
    order_status: Optional[str] = "PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
                "example": {
                    "order_status": "PENDING",
                }
            }


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    price: int

    class Config:
        orm_mode = True
        schema_extra = {
                "example": {
                    "name": "Example Product",
                    "price": 100,
                }
        }

