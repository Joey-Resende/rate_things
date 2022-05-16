import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from rate_things import models
from rate_things.config import settings

warnings.filterwarnings('ignore', category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
