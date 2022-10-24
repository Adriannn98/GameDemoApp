from random import randint, choice

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Hero(models.Model):
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    defence = models.IntegerField(default=10)
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"

class Monster(models.Model):
    name = models.CharField(max_length=64)
    hp = models.IntegerField(default=100)
    attack = models.IntegerField()
    defence = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class AliveMonster(models.Model):
    monster_class = models.ForeignKey(Monster, on_delete=models.CASCADE)
    current_hp = models.IntegerField(null=True)

    @property
    def attack(self):
        return self.monster_class.attack

    @property
    def defence(self):
        return self.monster_class.defence

    @property
    def name(self):
        return self.monster_class.name

class Game(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    level = models.IntegerField()
    monsters = models.ManyToManyField('AliveMonster', through='AlvieMonsterInGame')

class Stage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    monsters = models.ManyToManyField(AliveMonster, through='AlvieMonsterInStage')
    visited = models.BooleanField(default=False)
    next_stage = models.ForeignKey("Stage", on_delete=models.SET_NULL, null=True, related_name='prev')


    def generate_monsters(self):
        monster_list = Monster.objects.all()
        amount = 5
        for _ in range(amount):
            mc = choice(monster_list)
            extra_hp = randint(0,10)
            am = AliveMonster.objects.create(monster_class=mc, current_hp=mc.hp+extra_hp)
            AlvieMonsterInStage.objects.create(stage=self, monster=am)


class AlvieMonsterInGame(models.Model):
    monster = models.ForeignKey(AliveMonster, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class AlvieMonsterInStage(models.Model):
    monster = models.ForeignKey(AliveMonster, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
