# -- coding: utf-8 --

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse

from card.forms import CardForm, EptitudeForm, RaceForm, SubRaceForm, BookForm, AddBookOwnerForm
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.sites.models import get_current_site

from card.models import Card, CardEptitude, Race, SubRace, Book

from django.shortcuts import get_object_or_404

from hero.models import Hero

import logging
logger = logging.getLogger('common')

# Create your views here.
def create_card (request,
         template_name='card/create_card.html',
         card_form=CardForm,
         current_app=None,
         extra_context=None):

    redirect_to = "/cards/create/success"

    if request.method == "POST":
        form = card_form(request.POST)
        if form.is_valid():

            title = request.POST['title']
            attack = request.POST['attack']
            defense = request.POST['defense']
            price = request.POST['price']
            description = request.POST["description"]
            card_type = bool(int(request.POST["card_type"]))
            race_id = request.POST['race']
            book_id = request.POST['book']

            try :
                race = Race.objects.get(pk=race_id)
            except Race.DoesNotExist:
                race = None

            subrace_id = request.POST['subrace']
            try:
                subrace = SubRace.objects.get(pk=subrace_id)
            except SubRace.DoesNotExist:
                subrace = None

            try:
                book =Book.objects.get (pk=book_id)
            except Book.DoesNotExist:
                book = None


            card = Card.objects.create(
                title=title,
                attack=attack,
                defense=defense,
                price=price,
                description = description,
                card_type = card_type,
                race = race,
                subrace = subrace,
                book = book
            )

            if 'create_eptitude' in request.POST:
                redirect_to = "/cards/create_eptitude/%s" % card.id

            if 'create_race' in request.POST:
                redirect_to = '/cards/create_race/%s' % card.id

            if 'create_subrace' in request.POST:
                redirect_to = '/cards/create_subrace/%s' % card.id

            return HttpResponseRedirect(redirect_to)

    else:
        data = {"card_type":0}
        form = card_form(data)



    current_site = get_current_site(request)

    context = {
        'form': form,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

# Create your views here.
def create_card_for_book (request, book_id,
         template_name='card/create_card.html',
         card_form=CardForm,
         current_app=None,
         extra_context=None):

    book = get_object_or_404(Book, pk=book_id)

    redirect_to = "/cards/book/%s" % book_id

    if request.method == "POST":
        form = card_form(request.POST)
        if form.is_valid():

            title = request.POST['title']
            attack = request.POST['attack']
            defense = request.POST['defense']
            price = request.POST['price']
            description = request.POST["description"]
            card_type = bool(int(request.POST["card_type"]))
            race_id = request.POST['race']
            book_id = request.POST['book']

            try :
                race = Race.objects.get(pk=race_id)
            except Race.DoesNotExist:
                race = None

            subrace_id = request.POST['subrace']
            try:
                subrace = SubRace.objects.get(pk=subrace_id)
            except SubRace.DoesNotExist:
                subrace = None

            try:
                book =Book.objects.get (pk=book_id)
            except Book.DoesNotExist:
                book = None


            card = Card.objects.create(
                title=title,
                attack=attack,
                defense=defense,
                price=price,
                description = description,
                card_type = card_type,
                race = race,
                subrace = subrace,
                book = book
            )

            if 'create_eptitude' in request.POST:
                redirect_to = "/cards/create_eptitude/%s" % card.id

            if 'create_race' in request.POST:
                redirect_to = '/cards/create_race/%s' % card.id

            if 'create_subrace' in request.POST:
                redirect_to = '/cards/create_subrace/%s' % card.id

            return HttpResponseRedirect(redirect_to)

    else:
        data = {"card_type":0,
               "book":book.id,
        }
        form = card_form(data)



    current_site = get_current_site(request)

    context = {
        'form': form,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


def edit_card (request,card_id,
         template_name='card/edit_card.html',
         card_form=CardForm,
         current_app=None,
         extra_context=None):

    redirect_to = "/cards/list/"

    card = get_object_or_404(Card, pk=card_id)

    try:
        race_id =Race.objects.get (pk=card.race.id).id
    except ValueError:
        race_id = -1
    except AttributeError:
        race_id = -1

    try:
        subrace_id =SubRace.objects.get (pk=card.subrace.id).id
    except ValueError:
        subrace_id = -1
    except AttributeError:
        subrace_id = -1

    try:
        book_id =Book.objects.get (pk=card.book.id).id
    except ValueError:
        book_id = -1
    except AttributeError:
        book_id = -1

    data = {
        "title":card.title,
        "attack":card.attack,
        "defense":card.defense,
        "price":card.price,
        "description":card.description,
        "card_type":int(card.card_type),
        "race": race_id,
        "subrace":subrace_id,
        "book":book_id


    }

    if request.method == "POST":
        form = card_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            attack = request.POST['attack']
            defense = request.POST['defense']
            price = request.POST['price']
            description = request.POST["description"]
            card_type = bool(int(request.POST["card_type"]))
            race_id = request.POST['race']
            book_id = request.POST['book']

            try :
                race = Race.objects.get(pk=race_id)
            except Race.DoesNotExist:
                race = None

            subrace_id = request.POST['subrace']
            try:
                subrace = SubRace.objects.get(pk=subrace_id)
            except SubRace.DoesNotExist:
                subrace = None

            try:
                book = Book.objects.get(pk=book_id)
                redirect_to = "/cards/book/%s" % book_id
            except Book.DoesNotExist:
                book = None



            card.title = title
            card.attack = attack
            card.defense = defense
            card.price = price
            card.description = description
            card.card_type = card_type
            card.race = race
            card.subrace = subrace
            card.book = book
            card.save()

            if 'create_eptitude' in request.POST:
                redirect_to = "/cards/create_eptitude/%s" % card.id

            if 'create_race' in request.POST:
                redirect_to = '/cards/create_race/%s' % card.id

            if 'create_subrace' in request.POST:
                redirect_to = '/cards/create_subrace/%s' % card.id

            return HttpResponseRedirect(redirect_to)
    else:
        form = card_form(data)

    current_site = get_current_site(request)

    context = {
        'form': form,
        'site': current_site,
        'site_name': current_site.name,
        'eptitudes': card.eptitudes,
        'card':card,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

def success_created (
        request,
        template_name = 'card/success_created.html'):

     return TemplateResponse(request, template_name)

def success_edit_card (
        request,card_id,
        template_name='card/success_edit.html'):

    card = get_object_or_404(Card, pk=card_id)

    context = {
        'card': card
    }

    return TemplateResponse(request, template_name, context)


def delete_card(
        request,card_id,
        template_name='card/success_delete.html'):


    card = get_object_or_404(Card, pk=card_id)
    card_title = card.title
    card.delete()

    context = {
        'card_title': card_title
    }

    return TemplateResponse(request, template_name, context)

def cards_list (
        request,
        template_name = 'card/cards_list.html'):

    cards = Card.objects.all().order_by('price')

    context = {
        'cards': cards,
    }

    return TemplateResponse(request, template_name, context)

def books_list (
        request,
        template_name = 'card/books_list.html'):

    books = Book.objects.all()

    context = {
        'books': books,

    }

    return TemplateResponse(request, template_name, context)


def create_eptitude (
       request,card_id,
       eptitude_form = EptitudeForm,
       template_name='card/create_eptitude.html'):

    card = get_object_or_404(Card, pk=card_id)

    redirect_to = "/cards/edit/%s" % card_id

    if request.method == "POST":
        form = eptitude_form(card, request.POST)
        if form.is_valid():

            period = request.POST['period']
            level = request.POST['level']
            eptitude_type = request.POST['eptitude_type']
            power = request.POST["power"]

            race_id = request.POST['race']
            try :
                race = Race.objects.get(pk=race_id)
            except Race.DoesNotExist:
                race = None

            subrace_id = request.POST['subrace']
            try:
                subrace = SubRace.objects.get(pk=subrace_id)
            except SubRace.DoesNotExist:
                subrace = None

            unit_id = request.POST['unit']
            try :
                unit = Card.objects.get(pk=unit_id)
            except Card.DoesNotExist:
                unit = None

            dependency = request.POST['dependency']
            try :
                dependency_eptitude = CardEptitude.objects.get(pk=int(dependency))
            except CardEptitude.DoesNotExist:
                dependency_eptitude = None


            CardEptitude.objects.create(
                card = card,
                period = period,
                level = level,
                eptitude_type = eptitude_type,
                race = race,
                subrace = subrace,
                unit = unit,
                power = power,
                dependency = dependency_eptitude

            )


            return HttpResponseRedirect(redirect_to)
    else:
        form = eptitude_form(card)



    current_site = get_current_site(request)

    context = {
        'form': form,
        'site': current_site,
        'card': card,
        'site_name': current_site.name,
    }


    return TemplateResponse(request, template_name, context)


def edit_eptitude (
        request, card_id, eptitude_id,
        eptitude_form = EptitudeForm,
        template_name='card/edit_eptitude.html'):

     card = get_object_or_404(Card, pk=card_id)

     redirect_to = "/cards/edit/%s" % card_id

     eptitude = get_object_or_404(CardEptitude, pk=eptitude_id)

     if request.method == "POST":
        form = eptitude_form(card, request.POST)
        if form.is_valid():

            period = request.POST['period']
            level = request.POST['level']
            eptitude_type = request.POST['eptitude_type']
            power = request.POST["power"]


            race_id = request.POST['race']
            try :
                race = Race.objects.get(pk=race_id)
            except Race.DoesNotExist:
                race = None

            subrace_id = request.POST['subrace']
            try:
                subrace = SubRace.objects.get(pk=subrace_id)
            except SubRace.DoesNotExist:
                subrace = None

            unit_id = request.POST['unit']
            try :
                unit = Card.objects.get(pk=unit_id)
            except Card.DoesNotExist:
                unit = None

            dependency = request.POST['dependency']
            try :
                dependency_eptitude = CardEptitude.objects.get(pk=int(dependency))
            except CardEptitude.DoesNotExist:
                dependency_eptitude = None

            eptitude.period = period
            eptitude.level = level
            eptitude.eptitude_type = eptitude_type
            eptitude.race = race
            eptitude.subrace = subrace
            eptitude.unit = unit
            eptitude.power = power
            eptitude.dependency = dependency_eptitude
            eptitude.save()

            return HttpResponseRedirect(redirect_to)

     else:

        try:
                race_id =Race.objects.get (pk=eptitude.race.id).id
        except ValueError:
                race_id = -1
        except AttributeError:
                race_id = -1

        try:
              subrace_id =SubRace.objects.get (pk=eptitude.subrace.id).id
        except ValueError:
              subrace_id = -1
        except AttributeError:
              subrace_id = -1

        try:
              unit_id =Card.objects.get (pk=eptitude.unit.id).id
        except ValueError:
              unit_id = -1
        except AttributeError:
              unit_id = -1

        try:
            dependency = CardEptitude.objects.get(pk=eptitude.dependency.id).id
        except ValueError:
              dependency = -1
        except AttributeError:
              dependency = -1


        data = {
            "period":eptitude.period,
            "level":eptitude.level,
            "eptitude_type":eptitude.eptitude_type,
            "race":race_id,
            "subrace":subrace_id,
            "unit":unit_id,
            "power":eptitude.power,
            "dependency":dependency
        }
        form = eptitude_form(card, data)

     current_site = get_current_site(request)

     context = {
            'form': form,
            'card': card,
            'site': current_site,
            'site_name': current_site.name,
        }


     return TemplateResponse(request, template_name, context)

def create_race (request,
                 card_id,
                 race_form = RaceForm,
                 template_name = 'card/create_race.html'
):

     card = get_object_or_404(Card, pk=card_id)

     redirect_to = "/cards/edit/%s" % card_id

     if request.method == "POST":
        form = race_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST["description"]

            Race.objects.create(title=title, description=description)

            return HttpResponseRedirect(redirect_to)
     else:
        form = race_form()

     current_site = get_current_site(request)

     context = {
            'form': form,
            'site': current_site,
            'site_name': current_site.name,
        }


     return TemplateResponse(request, template_name, context)

def create_subrace (request,
                 card_id,
                 subrace_form = SubRaceForm,
                 template_name = 'card/create_subrace.html'
):

     card = get_object_or_404(Card, pk=card_id)

     redirect_to = "/cards/edit/%s" % card_id

     if request.method == "POST":
        form = subrace_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST["description"]
            race_id = request.POST['race']
            race = Race.objects.get(pk=race_id)

            SubRace.objects.create(title=title, description=description, race=race)

            return HttpResponseRedirect(redirect_to)
     else:
        form = subrace_form()

     current_site = get_current_site(request)

     context = {
            'form': form,
            'site': current_site,
            'site_name': current_site.name,
        }


     return TemplateResponse(request, template_name, context)


def create_book (request,
                 book_form = BookForm,
                 template_name = 'card/create_book.html'
                 ):

     redirect_to = "/cards/books/list/"

     if request.method == "POST":
        form = book_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']

            book = Book.objects.create(title=title, description=description)

            if 'add_book_owner' in request.POST:
                redirect_to = "/cards/add_book_owner/%s" % book.id


            return HttpResponseRedirect(redirect_to)
     else:
        form = book_form()

     context = {
            'form': form,

     }

     return TemplateResponse(request, template_name, context)

def add_book_owner (request,
                    book_id,
                    add_book_owner_form= AddBookOwnerForm,
                    template_name='card/add_book_owner.html'
                    ):


     book = get_object_or_404(Book, pk=book_id)

     redirect_to = "/cards/edit_book/%s" % book.id

     if request.method == "POST":
        form = add_book_owner_form(request.POST)
        if form.is_valid():

            hero_id = request.POST['hero']
            try:
                hero = Hero.objects.get(pk=hero_id)
                book.heroes.add (hero)
            except Hero.DoesNotExist:
                pass

            return HttpResponseRedirect(redirect_to)
     else:
        form = add_book_owner_form ()

     context = {
            'form': form,

     }

     return TemplateResponse(request, template_name, context)


def edit_book (request, book_id,
                 book_form = BookForm,
                 template_name = 'card/edit_book.html'
                 ):

     book = get_object_or_404(Book, pk=book_id)

     data = {
         "title":book.title,
         "description":book.description
     }

     redirect_to = "/cards/books/list/"

     if request.method == "POST":
        form = book_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']

            book.title=title
            book.description = description
            book.save()

            if 'add_book_owner' in request.POST:

                redirect_to = "/cards/add_book_owner/%s" % book.id


            return HttpResponseRedirect(redirect_to)
     else:
        form = book_form(data)

     context = {
            'form': form,
            'book':book,

     }

     return TemplateResponse(request, template_name, context)

def remove_book_owner (request,
                       book_id,
                       hero_id
                       ):
     book = get_object_or_404(Book, pk=book_id)
     hero = get_object_or_404(Hero, pk=hero_id)

     book.heroes.remove(hero)

     redirect_to = "/cards/edit_book/%s" % book.id
     return HttpResponseRedirect(redirect_to)



def delete_book (request, book_id):

    book = get_object_or_404(Book, pk=book_id)
    book.delete()

    redirect_to = "/cards/books/list/"

    return HttpResponseRedirect(redirect_to)


def book_cards (request, book_id,
          template_name = 'card/book.html'
          ):
    book = get_object_or_404(Book, pk=book_id)

    context = {
            'book': book,
            'cards':book.cards,
    }

    return TemplateResponse(request, template_name, context)
