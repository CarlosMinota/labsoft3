from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hola mundo! Estás en el index de control del proyecto!")
