import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # add_new_book()

    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2
        # косяк в примере, нет такого метода и словаря

        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_name_number_exception(self, collector):
        with pytest.raises(Exception):
            collector.add_new_book(123)

    @staticmethod
    def check_name(name_book):
        if len(name_book) < 1 or len(name_book) > 40:
            return False
        return True

    @pytest.mark.parametrize("name_book",
                             [
                                 "1",
                                 "123456789012345678901234567890123456789",
                                 "1234567890123456789012345678901234567890"
                             ])
    def test_add_new_book_with_name_book(self, name_book):
        assert self.check_name(name_book)

    def test_add_new_book_without_name_null_result(self, collector):
        collector.add_new_book("")

        assert len(collector.books_genre) == 0

    def test_add_new_book_41_number_null_result(self, collector):
        collector.add_new_book("12345678901234567890123456789012345678901")

        assert len(collector.books_genre) == 0

    def test_add_book_twice_one_book_in_result(self, collector):
        collector.add_new_book("probe")
        collector.add_new_book("probe")

        assert len(collector.books_genre) == 1

    # set_book_genre()

    def test_add_book_set_genre_in_list_genre_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe", "Ужасы")

        assert list(collector.books_genre.values())[0] == "Ужасы"

    def test_add_book_set_genre_not_in_list_genre_not_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe", "Ужасы1")

        assert list(collector.books_genre.values())[0] == ""

    def test_add_book_set_genre_wrong_book_genre_not_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe1", "Ужасы")

        assert list(collector.books_genre.values())[0] == ""

    def test_add_book_set_wrong_genre_in_wrong_book_genre_not_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe1", "Ужасы1")

        assert list(collector.books_genre.values())[0] == ""

    # get_book_genre()

    def test_get_book_genre_from_exist_book_genre_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe", "Ужасы")

        assert collector.get_book_genre("probe") == "Ужасы"

    def test_get_book_genre_from_nonexist_book_genre_not_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe1", "Ужасы")

        assert collector.get_book_genre("probe") == ""

    # get_books_with_specific_genre()

    def test_get_books_with_spec_genre_exist_book_exist_genre__genre_add(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe", "Ужасы")

        assert collector.get_books_with_specific_genre("Ужасы") == ["probe"]

    def test_get_books_with_spec_genre_nonexist_book_exist_genre_genre_not_add(self, collector):
        assert collector.get_books_with_specific_genre("Ужасы") == []

    # get_books_genre()

    def test_get_books_genre_from_one_exist_books(self, collector):
        collector.add_new_book("probe")
        collector.set_book_genre("probe", "Ужасы")

        assert collector.get_books_genre() == {'probe': 'Ужасы'}

    def test_get_books_genre_from_two_exist_books(self, collector):
        collector.add_new_book("probe")
        collector.add_new_book("probe1")
        collector.set_book_genre("probe", "Ужасы")
        collector.set_book_genre("probe1", "Мультфильмы")

        assert collector.get_books_genre() == {'probe': 'Ужасы', 'probe1': 'Мультфильмы'}

    def test_get_books_genre_from_nonexist_books_null_result(self, collector):
        assert collector.get_books_genre() == {}

    # get_books_for_children()

    def test_get_books_for_children_exist_(self, collector):
        collector.add_new_book("probe")
        collector.add_new_book("probe1")
        collector.set_book_genre("probe", "Ужасы")
        collector.set_book_genre("probe1", "Мультфильмы")

        assert collector.get_books_for_children() == ["probe1"]

    def test_get_books_for_children_nonexist(self, collector):
        collector.add_new_book("probe")
        collector.add_new_book("probe1")
        collector.set_book_genre("probe", "Ужасы")
        collector.set_book_genre("probe1", "Детективы")

        assert collector.get_books_for_children() == []

    # add_book_in_favorites()

    def test_add_book_in_favorites_exist_book_add_to_list(self, collector):
        collector.add_new_book("probe")
        collector.add_book_in_favorites("probe")

        assert collector.get_list_of_favorites_books() == ["probe"]

    def test_add_book_in_favorites_nonexist_book_nonadd_to_list(self, collector):
        collector.add_new_book("probe")
        collector.add_book_in_favorites("probe1")

        assert collector.get_list_of_favorites_books() == []

    # delete_book_from_favorites()

    def test_delete_book_from_favorites_nonexist_book_null_list(self, collector):
        collector.add_new_book("probe")
        collector.add_book_in_favorites("probe")
        collector.delete_book_from_favorites("probe1")

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_exist_book_null_list(self, collector):
        collector.add_new_book("probe")
        collector.add_book_in_favorites("probe")
        collector.delete_book_from_favorites("probe")

        assert len(collector.get_list_of_favorites_books()) == 0

    # get_list_of_favorites_books()

    def test_get_list_of_favorites_books_exist_books(self, collector):
        collector.add_new_book("probe")
        collector.add_new_book("probe1")
        collector.add_book_in_favorites("probe")
        collector.add_book_in_favorites("probe1")

        assert collector.get_list_of_favorites_books() == ["probe", "probe1"]
