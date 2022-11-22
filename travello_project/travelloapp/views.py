import django.contrib.auth.models
from django.shortcuts import render
from .models import place
from .models import meet_the_team


# Create your views here.
def index(request):
    obj = place.objects.all()
    obj1 = meet_the_team.objects.all()
    return render(request, "index.html", {'result': obj, 'meet_result': obj1})


