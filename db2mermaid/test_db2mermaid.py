import pytest
from db2mermaid.db2mermaid import DB2Mermaid as dm
from sqlalchemy import Column, Integer, String


def set_up():
    pass


def tear_down():
    pass


def test_integer(db2mermaid):
    column_data = Column(Integer, name="id")
    assert db2mermaid.create_row_per_column(column_data) == "        INTEGER id\n"


def test_string(db2mermaid):
    column_data = Column(String(length=45), name="id")
    assert db2mermaid.create_row_per_column(column_data) == "        VARCHAR(45) id\n"


def test_illegal_input(db2mermaid):
    column_data = Column(String, name="id")
    assert db2mermaid.create_row_per_column(column_data) != "        VARCHAR(45) id\n"


@pytest.fixture
def db2mermaid():
    return dm()


if __name__ == "__main__":
    pytest.main()
