from typing import Annotated, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base, str_256


intpk = Annotated[int, mapped_column(primary_key=True, index=True)]


class Category(Base):
    __tablename__ = 'categories'
    
    __table_args__ = {'extend_existing': True} 
    
    id: Mapped[intpk]
    name: Mapped[str_256]
    slug: Mapped[str_256] = mapped_column(unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=True) # New

    products: Mapped[List["Product"]] = relationship(back_populates="category")   # Для связи "один ко многим"


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[intpk]
    name: Mapped[str_256]
    slug: Mapped[str_256] = mapped_column(unique=True, index=True)
    description: Mapped[str_256]
    price: Mapped[int] 
    image_url: Mapped[str_256]
    stock: Mapped[int]
    supplier_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True) 
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id')) 
    rating: Mapped[float] 
    is_active: Mapped[bool] = mapped_column(default=True)

    category: Mapped["Category"] = relationship(back_populates='products') # Для связи "один ко многим"




class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[intpk]
    first_name: Mapped[str_256] # Поле имени пользователя.   
    last_name: Mapped[str_256] # Поле фамилии пользователя.

    user_name: Mapped[str_256] = mapped_column(unique=True) # поле логина пользователя.
    email_name: Mapped[str_256] = mapped_column(unique=True) # поле E-Mail пользователя.
    hashed_password: Mapped[str_256] # Поле хранения хэшированного пароля.
    
    #  Поля хранящие булевые значения, чтобы заблокировать доступ к некоторым разделам API
    is_active: Mapped[bool] = mapped_column(default=True) 
    is_admin: Mapped[bool] = mapped_column(default=False) 
    is_supplier: Mapped[bool] = mapped_column(default=False)
    is_customer: Mapped[bool] = mapped_column(default=True)
