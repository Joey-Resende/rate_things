from typing import Optional, List
from sqlmodel import select
from rate_things.database import get_sessions
from rate_things.models import Things


def add_things_to_database(
    things: str,
    name: str,
    gender: str,
    score: int,
    image: int,
    cost: int,
) -> bool:
    with get_sessions() as sessions:
        things = Things(
            things=things,
            name=name,
            gender=gender,
            score=score,
            image=image,
            cost=cost,
        )
        session.add(things)

    return True
