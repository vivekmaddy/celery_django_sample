from django.shortcuts import render
from django.http import HttpResponse

from .tasks import update_counter
# Create your views here.


def update_count(request):
    update_counter.delay()
    return HttpResponse("Celery delay started")