from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'user' #class Meta:    db_table = 'user
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(250), unique=True)
    password = Column(Text)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship("Order", back_populates='user')  # one to many relationship

    def __repr__(self):
        return f'<User(id={self.id}, username={self.username}, email={self.email})>'


class Product(Base):
    __tablename__= 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    price = Column(Integer)
    orders = relationship('Order', back_populates='product')  # Add this line

    def __repr__(self):
        return f'<Product(id={self.id}, name={self.name}, price={self.price})>'


class Order(Base):
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered'),
    )
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))  # 'users' to 'user'
    product_id = Column(Integer, ForeignKey('products.id'))
    status = Column(ChoiceType(ORDER_STATUS), default="PENDING")
    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')
    quanty = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Order(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, status={self.status})>'






