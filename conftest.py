import pytest
from main import BooksCollector


# фикстура для создания книги ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
@pytest.fixture(scope='function')
def books_genre():
    return {'Машина времени': "Фантастика",
            "Ложная слепота": "Фантастика",
            'Шерлок Холмс': 'Детективы'}


@pytest.fixture(scope='function')
def books_collections():
    books_collections = BooksCollector()
    books_collections.books_genre = {'Машина времени': "Фантастика",
                                     "Ложная слепота": "Фантастика",
                                     'Шерлок Холмс': 'Детективы'}
    return books_collections
