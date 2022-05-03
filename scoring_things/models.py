from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator
from statistics import mean
from datetime import datetime


class Things(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    things: str      # Que tipo de coisa estamos avaliando
    name: str        # O nome dessa coisa
    gender: str      # O genero dela
    score: int       # A nota para o conteudo
    image: int       # A nota para a apresentacao
    cost: int        # A nota para o custo/beneficio
    rate: int = 0
    date: datetime = Field(dafault_factory=datetime.now)

    @validator('score', 'image', 'cost')
    def validate_ratings(cls, score, field):
        if score < 1 or score > 10:
            raise RuntimeError(f'{field.name} must be between 1 and 10')
        return score

    @validator('rate', always=True)
    def calculate_rate(cls, score, values):
        rate = mean([values['score'], values['image'], values['cost']])
        return int(rate)
