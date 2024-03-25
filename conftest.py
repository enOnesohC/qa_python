import pytest

from main import BooksCollector


@pytest.fixture()  # создание ЭК
def collector():
    collector = BooksCollector()
    return collector
