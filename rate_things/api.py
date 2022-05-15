from typing import List
from fastapi import FastAPI
from rate_things.core import get_things_from_database
from rate_things.serializers import ThingsIn, ThingsOut
from rate_things.database import get_session
from rate_things.models import Things

api = FastAPI(title="rate_things")


@api.get('/things/', response_model=List[ThingsOut])
def list_things():
    things = get_things_from_database()
    return things


@api.post('/things/', response_model=ThingsIn)
def add_things(things_in: ThingsIn):
    things = Thing(**things_in.dict())
    with get_session() as session:
        session.add(things)
        session.commit()
        session.refresh(things)
        return things
