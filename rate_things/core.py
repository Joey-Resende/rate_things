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
        sessions.add(things)

    return True


def get_things_from_database() -> List[Things]:
    with get_sessions() as sessions:
        sql = select(Things)
        return sessions.exec(sql)
