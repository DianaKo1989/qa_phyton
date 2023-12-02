import pytest


books_name_and_genre = [["1984", "Фантастика"], ["Зов Ктулху", "Ужасы"], ["Дракула", "Ужасы"], ["Трое в лодке", "Комедии"]]
books_name = [book[0] for book in books_name_and_genre]
books_genre = set([book[1] for book in books_name_and_genre])
books_by_genre= dict()
for name, genre in books_name_and_genre:
    if genre not in books_by_genre:
        books_by_genre[genre] = []
    books_by_genre[genre].append(name)


@pytest.mark.parametrize("name", books_name)
def test_add_new_book_name_is_in_book_genre(books_collector, name):
    books_collector.add_new_book(name)
    assert name == books_collector.get_books_genre(name)


@pytest.mark.parametrize("name", books_name)
def test_get_book_genre_none(books_collector, name):
    assert books_collector.get_books_genre(name) is None


@pytest.mark.parametrize("name, genre", books_name_and_genre)
def test_get_book_genre_is_equal(books_collector, name, genre):
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert genre == books_collector.get_book_genre(name)


@pytest.mark.parametrize("genre", books_genre)
def test_get_books_with_specific_genre_books_list(books_collector, genre):
    for book_name, book_genre in books_name_and_genre:
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)
    for book_name in books_by_genre[genre]:
        assert book_name in books_collector.get_books_with_specific_genre(genre)



@pytest.mark.parametrize("genre", books_genre)
def test_get_books_with_specific_genre_empty(books_collector, genre):
    for book_name in books_by_genre[genre]:
        assert len(books_collector.get_books_with_specific_genre(genre)) == 0


@pytest.mark.parametrize("name, genre", [["1984", "Фантастика"], ["Трое в лодке", "Комедии"]])
def test_get_books_for_children_books_list(books_collector, name, genre):
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert name in books_collector.get_books_for_children()


@pytest.mark.parametrize("name, genre", [["Зов Ктулху", "Ужасы"], ["Дракула", "Ужасы"]])
def test_get_books_for_children_empty_list(books_collector, name, genre):
    books_collector.add_new_book(name)
    books_collector.set_book_genre(name, genre)
    assert len(books_collector.get_books_for_children()) == 0


@pytest.mark.parametrize("name", books_name)
def test_get_list_of_favorites_books_empty_list(books_collector, name):
    assert len(books_collector.get_list_of_favorites_books()) == 0


@pytest.mark.parametrize("name", books_name)
def test_add_book_in_favorites_is_in_favorites_books(books_collector, name):
    books_collector.add_book_in_favorites(name)
    assert name in books_collector.get_list_of_favorites_books()


@pytest.mark.parametrize("name", books_name)
def test_delete_book_from_favorites_empty_list(books_collector, name):
    books_collector.add_book_in_favorites(name)
    books_collector.delete_book_from_favorites(name)
    assert len(books_collector.get_list_of_favorites_books()) == 0


