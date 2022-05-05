from sqlmodel import create_engine
from rate_things.config import settings
from rate_things import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)
