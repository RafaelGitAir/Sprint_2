import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def book(self):
        self.book = 'Машина времени'
        return self.book

    # тестирование метода __init__
    def test_list_of_genre_true(self):
        collection_of_book = BooksCollector()
        assert collection_of_book.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # позитивное тестирование метода add_new_book
    def test_add_new_book_book_with_acceptable_name_true(self):
        collection_of_book = BooksCollector()
        collection_of_book.add_new_book(self.book)
        assert 'Машина времени' in collection_of_book.books_genre

    # негативное тестирование метода add_new_book
    negative_case_book = ['', 'f' * 41]

    @pytest.mark.parametrize('wrong_book', negative_case_book)
    def test_add_new_book_new_book_with_wrong_name_empty_dict(self, wrong_book):
        collection_of_book = BooksCollector()
        collection_of_book.add_new_book(wrong_book)
        assert collection_of_book.books_genre == {}

    # позитивная проверка метода set_book_genre
    def test_set_book_genre_exist_genre_true(self):
        collection_of_book = BooksCollector()
        collection_of_book.add_new_book(self.book)
        genre = 'Фантастика'
        collection_of_book.set_book_genre(self.book, genre)
        assert collection_of_book.books_genre[self.book] == 'Фантастика'

    # негативаня проверка метода set_book_genre
    def test_set_book_genre_wrong_genre_empty_string_genre(self):
        collection_of_book = BooksCollector()
        collection_of_book.add_new_book(self.book)
        genre = 'Роман'
        collection_of_book.set_book_genre(self.book, genre)
        assert collection_of_book.books_genre[self.book] == ''

    # позитивная проверка метода get_book_genre
    def test_get_book_genre_exist_book_with_exist_genre_true(self, books_collections):
        book_check = "Ложная слепота"
        assert books_collections.get_book_genre(book_check) == 'Фантастика'

    # позитивная проверка метода get_books_with_specific_genre
    def test_get_books_with_specific_genre_exist_genre_true(self, books_collections):
        specific_genre = "Фантастика"
        books_with_specific_genre = books_collections.get_books_with_specific_genre(specific_genre)
        assert len(books_with_specific_genre) == 2

    # позитивная проверка метода get_books_genre
    def test_get_books_genre_exist_dict_books_true(self, books_collections):
        check_dict_books_genre = books_collections.get_books_genre()
        assert check_dict_books_genre == {'Машина времени': "Фантастика",
                                          "Ложная слепота": "Фантастика",
                                          'Шерлок Холмс': 'Детективы'}

    # позитивная проверка метода get_books_for_children
    def test_get_books_for_children(self, books_collections):
        books_for_children = books_collections.get_books_for_children()
        assert books_for_children == ['Машина времени', 'Ложная слепота']

    # позитивная проверка метода add_book_in_favorites
    def test_add_book_in_favorites_exist_book_book_in_favorites(self, books_collections):
        book = 'Шерлок Холмс'
        books_collections.add_book_in_favorites(book)
        assert books_collections.favorites == ['Шерлок Холмс']

    def test_delete_book_from_favorites_exist_favorites_empty_favorites(self, books_collections):
        book = 'Шерлок Холмс'
        books_collections.add_book_in_favorites(book)
        books_collections.delete_book_from_favorites(book)
        assert books_collections.favorites == []

    def test_get_list_of_favorites_books_exist_favorites_favorites_list(self, books_collections):
        book = 'Шерлок Холмс'
        books_collections.add_book_in_favorites(book)
        favorite_list = books_collections.get_list_of_favorites_books()
        assert favorite_list == ['Шерлок Холмс']


