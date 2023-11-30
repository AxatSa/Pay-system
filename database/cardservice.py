from datetime import datetime
from sqlalchemy.orm import Session
from database.models import Card, User
from database import get_db


def add_card_db(user_id, card_number, balance, card_name, exp_date):
    db = next(get_db())

    new_card = Card(user_id=user_id, card_number=card_number, balance=balance,
                    card_name=card_name, exp_date=exp_date)

    db.add(new_card)
    db.commit()

    return 'Пользователь успешно зарегался'


def delete_card_db():
    db = next(get_db())

    delete_cards = db.query(Card).filter_by(card_id=card_id).first()

    if delete_cards:
        db.delete(delete_cards)
        db.commit()

        return 'Карта удалена'

    else:
        return 'Карта не найден'


def get_exact_user_cards_db(user_id):
    db = next(get_db())

    exact_db = db.query(Card).filter_by(user_id=user_id).first()

    pass


def get_exact_card_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).fitst()

    return checker


def get_check_card_info_db(user_id, card_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        cards = db.query(Card).filter_by(user_id=user_id).all()

        return cards
    else:
        return 'Пользователь не найден'
