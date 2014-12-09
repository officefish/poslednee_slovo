# -- coding: utf-8 --
from django.db import models
from django.contrib.auth.models import User

from hero.models import Hero

class Book (models.Model):
    title = models.CharField (max_length=70)
    description = models.CharField (max_length=200)
    heroes = models.ManyToManyField(Hero, blank=True, null=True, related_name='heroes')


    @property
    def cards(self):
        return self.card_set.all().order_by('price')

class Race (models.Model):
    title = models.CharField (max_length=70)
    description = models.CharField (max_length=200)

class SubRace (models.Model):
    race = models.ForeignKey (Race)
    title = models.CharField (max_length=70)
    description = models.CharField(max_length=200)

# Create your models here.
class Card (models.Model):
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    title = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    description = models.CharField (max_length=200)
    # if False type is eptitude. if True type is unit
    card_type = models.BooleanField (default=True)
    unit_type = models.CharField(max_length=70)
    race = models.ForeignKey(Race, blank= True, null=True)
    subrace = models.ForeignKey (SubRace, blank=True, null=True)
    book = models.ForeignKey (Book, blank=True, null=True)


    @property
    def eptitudes(self):
        return self.cardeptitude_set.all()

class CardEptitude (models.Model):

     card = models.ForeignKey(Card)

     # Момент использования уникальной способности
     # 0 - ставится на поле
     # 1 - умирает
     # 2 - получает ранение
     # 3 - в начале хода
     # 4 - в конце хода
     period = models.IntegerField(default=0)


     # Уровень использования уникальной способности
     # 0 - к самому себе
     # 1 - к двум соседям
     # 2 - к своему герою
     # 3 - ко всем своим
     # 4 - к выбранному своему
     # 5 - к случайному своему
     # 6 - к герою врага
     # 7 - ко все врагам
     # 8 - к выбранному врагу
     # 9 -к случайному врагу
     # 10 - ко всем юнитам на поле
     # 11 - к своим юнитам определенного типа
     # 12 - к вражеским юнитам определенного типа
     # 13 - ко всем юнитам определенного типа на поле
     # 14 - к случайному юниту на поле
     # 15 - к случайному юниту определенного типа на поле
     # 16 - к своему случайному юниту определенного типа
     # 17 - к вражескому юниту определенного типа
     # 18 - своя колода
     # 19 - колода противника

     level = models.IntegerField(default=0)

     # Вид уникальной способности
     # 0 - лечение
     # 1 - увеличение здоровья
     # 2 - уменьшение здоровья
     # 3 - увеличение аттаки
     # 4 - уменьшение аттаки
     # 5 - пассивная аттака
     # 6 - рывок
     # 7 - провокация
     # 8 - засада
     # 9 - новый юнит
     # 10 - новая карта
     # 11 - карта из колоды
     # 12 - активация
     # 13 - полное восстановление здоровья
     # 14 - убийство
     # 15 - двойная аттака
     # 16 - немота
     # 17 - заморозка

     eptitude_type = models.IntegerField(default=0)

     unit = models.ForeignKey(Card, blank=True, null=True, related_name='unit')
     race = models.ForeignKey(Race, blank= True, null=True)
     subrace = models.ForeignKey (SubRace, blank=True, null=True)

     power = models.IntegerField(default=0)
     dependency = models.ForeignKey('self',blank= True, null=True)



class Collection (models.Model):
    owner = models.ForeignKey (User, related_name='collection_owner')
    cards = models.ManyToManyField (Card, through='Collector')
    max_length = models.IntegerField(default=35)

class Collector (models.Model):
    card = models.ForeignKey (Card, related_name='collection_card')
    collection_list = models.ForeignKey (Collection)

