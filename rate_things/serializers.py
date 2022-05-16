from datetime import datetime
from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class ThingsOut(BaseModel):
    id: int
    things: str
    name: str
    gender: str
    score: int
    image: int
    cost: int
    rate: int
    date: datetime


class ThingsIn(BaseModel):
    things: str
    name: str
    gender: str
    score: int
    image: int
    cost: int

    @validator('score', 'image', 'cost')
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f'{field.name} must be between 1 and 10', status_code=status.HTTP_400_BAD_REQUEST
            )
        return v
