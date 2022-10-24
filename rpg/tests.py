import pytest
import pytest
from django.test import Client
from django.urls import reverse

from rpg.forms import HeroCreateForm, MonsterCreateForm
from rpg.models import Hero, Monster, Game


def test_index():
    client = Client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    assert 'Gra RPG' in str(response.content)


def test_add_hero_get():
    client = Client()
    url = reverse('create_hero')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, HeroCreateForm)

@pytest.mark.django_db
def test_add_hero_post():
    client = Client()
    url = reverse('create_hero')
    data = {
        'name':'adrian',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Hero.objects.get(name='adrian')


@pytest.mark.django_db
def test_all_heroes_get(heroes):
    client = Client()
    url = reverse('hero_list')
    response = client.get(url)
    assert response.status_code == 200
    heroes_form_view = response.context['all_heroes']
    assert heroes_form_view.count() == len(heroes)


def test_add_monster_get():
    client = Client()
    url = reverse('create_monster')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, MonsterCreateForm)

@pytest.mark.django_db
def test_add_monster_post():
    client = Client()
    url = reverse('create_monster')
    data = {
        'name':'Potwor',
        'hp': 100,
        'attack': 0,
        'defence': 0,

    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Monster.objects.get(name='Potwor')


@pytest.mark.django_db
def test_all_monster_get(monsters):
    client = Client()
    url = reverse('monster_list')
    response = client.get(url)
    assert response.status_code == 200
    monsters_form_view = response.context['all_monsters']
    assert monsters_form_view.count() == len(monsters)

@pytest.mark.django_db
def test_create_game_post(hero):
    client = Client()
    url = reverse('create_game')
    data = {
        'hero': hero.id,
        'level': 10,

    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Game.objects.get(level=10, hero=hero)

@pytest.mark.django_db
def test_create_game_for_hero(hero, user):
    client = Client()
    client.force_login(user)
    url = reverse('create_game_for_hero', args=(hero.id,))
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('game_detail', args=(Game.objects.get(hero=hero).id, ))
    assert response.url.startswith(url)