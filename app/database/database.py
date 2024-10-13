from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(settings.ASYNC_DATABASE_URL)
session_maker = sessionmaker(engine)

class Base(DeclarativeBase):
    pass


def create_database():
    Base.metadata.create_all(bind=engine)
