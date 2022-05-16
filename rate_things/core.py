from typing import Optional, List
from sqlmodel import select
from rate_things.database import get_session
from rate_things.models import Things


def add_things_to_database(
    things: str,
    name: str,
    gender: str,
    score: int,
    image: int,
    cost: int,
) -> bool:
    with get_session() as session:
        thing = Things(**locals())
        session.add(thing)
        session.commit()

    return True


def get_things_from_database(style: Optional[str] = None) -> List[Things]:
    with get_session() as session:
        sql = select(Things)
        if style:
            sql = sql.where(Things.style == style)
        return list(session.exec(sql))
