from django.http import HttpResponse
from django.shortcuts import render
from cources.models.cource import *

def index(request):
    cources = Cource.objects.all()
    data = {'cources':cources}
    return render(request, 'cources/index.html', data)