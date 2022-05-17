from unittest.mock import patch

import pytest
from sqlmodel import create_engine

from rate_things import models


@pytest.fixture(autouse=True, scope='function')
def each_test_uses_separate_database(request):
    tmpdir = request.getfixturevalue('tmpdir')
    test_db = tmpdir.join('rate.things.test.db')
    engine = create_engine(f'sqlite:///{test_db}')
    models.SQLModel.metadata.create_all(bind=engine)
    with patch('rate_things.database.engine', engine):
        yield
