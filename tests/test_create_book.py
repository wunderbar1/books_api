import pytest
from api.models import Book


@pytest.mark.filterwarnings
@pytest.mark.django_db
def test_book_model():
    book = Book.objects.create(title="Pan")
    assert book.title == "Pan"
    assert Book.objects.count() == 1


@pytest.mark.filterwarnings
@pytest.mark.django_db
def test_book_models_count():
    Book.objects.create(title="Pan")
    Book.objects.create(title="Pan 2")
    assert Book.objects.count() == 2


