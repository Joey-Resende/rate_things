import typer
from typing import Optional
from rate_things.core import add_things_to_database, get_things_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help='Rate_Things')

console = Console()


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
def list_things(things: Optional[str] = None):
    """Lists things in databese."""
    things = get_things_from_database()
    table = Table(title=':thunder: Rate_Things :thunder:')
    headers = ['id', 'things', 'name', 'gender',
               'score', 'image', 'cost', 'rate' 'date']
    for header in headers:
        table.add_column(header, style='blue')
    for thing in things:
        thing.date = Things.date.strftime("%Y-%m-%d")
        values = [str(getattr(thing, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
