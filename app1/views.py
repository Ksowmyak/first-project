from django.shortcuts import render
from django.http import HttpResponse
def paneer(request):
    return HttpResponse('paneer is ready')

def momos(request):
    return HttpResponse('momos is ready')


# Create your views here.
                             