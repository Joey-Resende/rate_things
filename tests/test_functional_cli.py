from typer.testing import CliRunner
from rate_things.cli import main

runner = CliRunner()


def test_add_thing():
    result = runner.invoke(main, [
                           'add', 'Serie', 'Cavaleiro da Lua', 'Heroi', '--score=7', '--image=7', '--cost=7'])
    assert result.exit_code == 0
    assert 'Things added' in result.stdout
    