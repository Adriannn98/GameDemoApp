import pytest
from django.contrib.auth.models import User

from rpg.models import Hero, Monster, Game


@pytest.fixture
def heroes():
    lst = []
    for x in range(10):
        lst.append(Hero.objects.create(name=x))
    return lst

@pytest.fixture
def monsters():
    lst = []
    for x in range(10):
        lst.append(Monster.objects.create(name=x, hp=100, attack=x*2, defence=x*3))
    return lst

@pytest.fixture
def hero():
    return Hero.objects.create(name='Thor')

@pytest.fixture
def user():
    return User.objects.create(username='test')