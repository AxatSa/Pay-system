from sqlalchemy import Column, DateTime, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Создание таблицы пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


class Card(Base):
    __tablename__ = 'user_cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_number = Column(Integer, nullable=False)
    balance = Column(Float, default=0)
    exp_date = Column(Integer, nullable=False)
    card_name = Column(String)

    user_fk = relationship(User, lazy='subquery')


class Trans(Base):
    __tablename__ = 'transfers'
    trans_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey('user_cards.card_id'))
    card_to_id = Column(Integer, ForeignKey('user_cards.card_id'))
    amount = Column(Float)

    status = Column(Boolean, default=True)

    trans_date = Column(DateTime)

    card_from_fk = relationship(Card, foreign_keys=[card_from_id], lazy='subquery')
    card_to_fk = relationship(Card, foreign_keys=[card_to_id], lazy='subquery')
