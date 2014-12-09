from django.shortcuts import render

# Create your views here.
from hero.models import Hero
from hero.forms import HeroForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


def heroes_list (request,
                 template_name='hero/heroes_list.html'
                ):

    heroes = Hero.objects.all()

    context = {
        'heroes': heroes,

    }

    return TemplateResponse(request, template_name, context)

def create_hero (request,
                 hero_form = HeroForm,
                 template_name =  'hero/create_hero.html'
                 ):

     redirect_to = "/heroes/list"

     if request.method == "POST":
        form = hero_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            vocation = request.POST["vocation"]
            eptitude = request.POST["eptitude"]
            price = request.POST['price']
            description = request.POST['description']

            hero = Hero.objects.create (
                title=title,
                vocation=vocation,
                eptitude= int(eptitude),
                price= int (price),
                description = description
            )

            return HttpResponseRedirect(redirect_to)

     else:
        form = hero_form()

     context = {
            'form': form,
     }


     return TemplateResponse(request, template_name, context)

def edit_hero (request,hero_id,
         template_name='hero/edit_hero.html',
         hero_form=HeroForm,
         ):

    redirect_to = "/heroes/list"

    hero = get_object_or_404(Hero, pk=hero_id)

    data = {
        "title":hero.title,
        "vocation":hero.vocation,
        "price":hero.price,
        "description":hero.description,
        "eptitude":hero.eptitude,
    }

    if request.method == "POST":
        form = hero_form(request.POST)
        if form.is_valid():
            title = request.POST['title']
            vocation = request.POST["vocation"]
            eptitude = request.POST["eptitude"]
            price = request.POST['price']
            description = request.POST['description']

            hero.title=title
            hero.vocation = vocation
            hero.eptitude = eptitude
            hero.price= price
            hero.description = description
            hero.save()

            return HttpResponseRedirect(redirect_to)
    else:
        form = hero_form(data)


    context = {
        'form': form,

    }

    return TemplateResponse(request, template_name, context)

def delete_hero (request,hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    hero.delete()
    redirect_to = "/heroes/list"

    return HttpResponseRedirect(redirect_to)
