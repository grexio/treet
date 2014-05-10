from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from market.models import Treet

@login_required
def home(request):
    treets = Treet.objects.all()
    return render(request, "core/home.html", {'treets': treets})
