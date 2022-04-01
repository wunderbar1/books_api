import pytest
from django.contrib.auth.models import User


@pytest.mark.skip("for now")
@pytest.mark.django_db
class TestUsers:
    pytestmark = pytest.mark.django_db

    def test_my_user(self):
        me = User.objects.get(username='bart')
        assert me.is_superuser
