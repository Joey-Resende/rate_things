from rate_things.core import get_things_from_database, add_things_to_database


def test_add_things_to_database():
    assert add_things_to_database(
        'Filme', 'Doutor Estranho II', 'Heroi', 8, 10, 8)


def test_get_things_to_database():
    add_things_to_database(
        'Filme', 'Doutor Estranho II', 'Heroi', 8, 10, 8)
    results = get_things_from_database()
    assert len(results) > 0
