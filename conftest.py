import pytest
from books_collector import BooksCollector

@pytest.fixture
def books_collector():
    books_collector = BooksCollector()
    return books_collector
