#! /usr/bin/env python
# -*- coding: utf-8 -*-



__author__ = 'inozemcev'
from django import forms
from card.models import Card, Race, SubRace, Book
from hero.models import Hero
from django.forms.extras.widgets import SelectDateWidget

CARD_TYPE_CHOISES=[
    ('0','способность'),
    ('1','персонаж')
]

# Момент использования уникальной способности
# 0 - ставится на поле
# 1 - умирает
# 2 - получает ранение
# 3 - в начале хода
# 4 - в конце хода
EPTITUDE_PERIOD_CHOISES=[
    ('0','ставится на поле'),
    ('1','умирает'),
    ('2','получает ранение'),
    ('3','в начале хода'),
    ('4','в конце хода'),
]


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

EPTITUDE_LEVEL_CHOISES=[
    ('0','к самому себе'),
    ('1','к двум соседям'),
    ('2','к своему герою'),
    ('3','ко всем своим персонажам на поле'),
    ('4','к выбранному своему персонажу'),
    ('5','к случайному своему персонажу'),
    ('6','к герою врага'),
    ('7','ко всем врагам'),
    ('8','к выбранному врагу'),
    ('9','к случайному врагу'),
    ('10', "ко всем юнитам на поле"),
    ('11','к своим юнитам определенного типа'),
    ('12','к вражеским юнитам определенного типа'),
    ('13', "ко всем юнитам определенного типа на поле"),
    ('14', "к случайному юниту на поле"),
    ('15', "к случайному юниту определенного типа на поле"),
    ('16', "к своему случайному юниту определенного типа"),
    ('17', "к вражескому юниту определенного типа"),
    ('18', "своя колода"),
    ('19', "колода противника"),
]


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
     # 16 - случайная карта из колоды противника

EPTITUDE_TYPE_CHOISES=[
    ('0','лечение'),
    ('1','увеличение здоровья'),
    ('2','уменьшение здоровья'),
    ('3','увеличение аттаки'),
    ('4','уменьшение аттаки'),
    ('5','пассивная аттака'),
    ('6','рывок'),
    ('7','провокация'),
    ('8','засада'),
    ('9','новый юнит'),
    ('10','новая карта'),
    ('11', "карта из колоды"),
    ('12', "активация"),
    ('13', "полное восстановление здоровья"),
    ('14', "убийство"),
    ('15', "двойная аттака"),
    ('16', "немота"),
    ('17', "заморозка")
]

etc = [
    'лечение',
    'увеличение здоровья',
    'уменьшение здоровья',
    'увеличение аттаки',
    'уменьшение аттаки',
    'пассивная аттака',
    'рывок',
    'провокация',
    'засада',
    'новый юнит',
    'новая карта',
    "карта из колоды",
    "активация",
    "полное восстановление здоровья",
    "убийство",
    "двойная аттака",
    "немота",
    "заморозка"
]


class CardForm (forms.Form):

      title = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'maxlength':70}))
      attack = forms.IntegerField(max_value=30, widget=forms.TextInput(attrs={'maxlength':2}))
      defense = forms.IntegerField(max_value=30, widget=forms.TextInput(attrs={'maxlength':2}))
      price = forms.IntegerField(max_value=12, widget=forms.TextInput(attrs={'maxlength':2}))
      description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'maxlength':200}))
      card_type = forms.ChoiceField(choices=CARD_TYPE_CHOISES, widget=forms.RadioSelect())


      def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)

        race_choises = [(-1, '----')]
        race_choises += [ (o.id, str(o.title)) for o in Race.objects.all()]

        self.fields['race'] = forms.ChoiceField(required=False, choices=race_choises)

        subrace_choises = [(-1, '----')]
        subrace_choises += [ (o.id, str(o.title)) for o in SubRace.objects.all()]

        self.fields['subrace'] = forms.ChoiceField(required=False, choices=subrace_choises)

        book_choises = [(-1, '----')]
        book_choises += [ (o.id, o.title) for o in Book.objects.all()]

        self.fields ['book'] =  forms.ChoiceField(required=False, choices=book_choises)


class RaceForm (forms.Form):
     title = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'maxlength':70}))
     description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'maxlength':200}))



class SubRaceForm (forms.Form):
     title = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'maxlength':70}))
     description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'maxlength':200}))

     def __init__(self, *args, **kwargs):
        super(SubRaceForm, self).__init__(*args, **kwargs)

        race_choises = [(-1, '----')]
        race_choises += [ (o.id, str(o.title)) for o in Race.objects.all()]

        self.fields['race'] = forms.ChoiceField(required=False, choices=race_choises)

class EptitudeForm (forms.Form):

    period = forms.ChoiceField(choices=EPTITUDE_PERIOD_CHOISES)
    level = forms.ChoiceField(choices=EPTITUDE_LEVEL_CHOISES)
    eptitude_type = forms.ChoiceField(choices=EPTITUDE_TYPE_CHOISES)
    power = forms.IntegerField(max_value=12, widget=forms.TextInput(attrs={'maxlength':2}))


    def __init__(self, card, *args, **kwargs):
        super(EptitudeForm, self).__init__(*args, **kwargs)

        race_choises = [(-1, '----')]
        race_choises += [ (o.id, str(o.title)) for o in Race.objects.all()]

        self.fields['race'] = forms.ChoiceField(required=False, choices=race_choises)

        subrace_choises = [(-1, '----')]
        subrace_choises += [ (o.id, str(o.title)) for o in SubRace.objects.all()]

        self.fields['subrace'] = forms.ChoiceField(required=False, choices=subrace_choises)

        unit_choises = [(-1, '----')]
        unit_choises += [ (o.id, o.title) for o in Card.objects.all()]

        self.fields['unit'] = forms.ChoiceField(required=False, choices=unit_choises)

        eptitude_choises = [(-1, '----')]
        eptitude_choises += [ (o.id, etc[o.eptitude_type]) for o in card.eptitudes]
        self.fields['dependency'] = forms.ChoiceField(required=False, choices=eptitude_choises)

class BookForm (forms.Form):
    title = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'maxlength':70}))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'maxlength':200}))


class AddBookOwnerForm (forms.Form):

      def __init__(self, *args, **kwargs):
        super(AddBookOwnerForm, self).__init__(*args, **kwargs)

        hero_choises = [(-1, '----')]
        hero_choises += [ (o.id, str(o.title)) for o in Hero.objects.all()]

        self.fields['hero'] = forms.ChoiceField(choices=hero_choises)

