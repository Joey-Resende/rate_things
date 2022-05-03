from sqlmodel import create_engine
from scoring_things.config import settings
from scoring_things import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)
