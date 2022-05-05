from rate_things import models
from rate_things.config import settings
from sqlmodel import create_engine, Session
import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar
warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)


def get_sessions():
    return Session(engine)
