from fastapi import FastAPI
from rate_things.core import get_things_from_database

api = FastAPI(title="rate_things")


@api.get('/things/')
def list_things():
    things = get_things_from_database()
    return things
