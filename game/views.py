# Create your views here.
from django.shortcuts import render


def crossdomain(request, **kwargs):
    return render(request, 'crossdomain.xml', {})