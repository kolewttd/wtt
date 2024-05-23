from django.http import HttpResponse
from wtt import wtt

def index(request):
    return HttpResponse(wtt.py)
