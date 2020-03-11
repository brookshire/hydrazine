from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext


def hydrazine_home(request):
    return render(request, 'home.html', context={
        "title": "Hydrazine",
        "greetings": "Hydrazine Prototype"
    })