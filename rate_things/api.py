from typing import List, Optional
from fastapi import FastAPI, Response, status
from rate_things.core import get_things_from_database
from rate_things.serializers import ThingsIn, ThingsOut
from rate_things.database import get_session
from rate_things.models import Things

api = FastAPI(title='rate_things')


@api.get('/things', response_model=List[ThingsOut])
async def list_things(style: Optional[str] = None):
    """Lists things from the database"""
    things = get_things_from_database(style)
    return things


@api.post('/things', response_model=ThingsOut)
async def add_things(things_in: ThingsIn, response: Response):
    things = Thing(**things_in.dict())
    with get_session() as session:
        session.add(things)
        session.commit()
        session.refresh(things)

    response.status_code = status.HTTP_201_CREATED
    return things
