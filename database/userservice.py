from datetime import datetime
from database.models import User
from database import get_db


def register_user_db(name, surname, email, password, city, phone_number, reg_date):
    db = next(get_db())

    new_user = User(name=name, last_name=surname, email=email, password=password,
                    city=city, phone_number=phone_number, reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return 'Пользователь зареган'


def get_exact_user_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()

    return checker


def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return {'message': 'Not found'}


def delete_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        db.delete(exact_user)
        db.commit()

        return 'Пользователь удален'

    else:
        return 'Пользователь не найден'


def get_all_user_db():
    db = next(get_db())

    users = db.query(User).all()

    return users
