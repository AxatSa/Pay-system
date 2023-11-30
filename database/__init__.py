from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHMEY_DATABASE_URI = 'sqlite:///pay.db'

engine = create_engine(SQLALCHMEY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

from database import models


# ФУнкция для генерации связей е базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback
        raise
    finally:
        db.close()
