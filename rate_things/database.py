from sqlmodel import create_engine, Session
from rate_things.config import settings
from rate_things import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_sessions():
    return Session(engine)
