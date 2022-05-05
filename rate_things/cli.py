import typer
from rate_things.core import add_things_to_database

main = typer.Typer(help='Rate_Things')


@main.command('add')
def add(
    things: str,
    name: str,
    gender: str,
    score: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new thing to database."""
    if add_things_to_database(things, name, gender, score, image, cost):
        print('⚡ Things added to database!')
    else:
        print('⛈️ deu ruim')


@main.command('list')
def list_things(name: str):
    """Lists things in databese."""
    print(name)
