from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404

from market.models import Treet
from market.forms import TreetCreationForm


@login_required
def new_treet(request):
    if request.method == 'POST':
        form = TreetCreationForm(request.POST)
        if form.is_valid():
            treet = form.save(commit=False)
            treet.user = request.user
            treet.save()
            messages.success(request, "Your treat was successfully added.")
            return redirect("home")
    else:
        form = TreetCreationForm()
    return render(request, "market/add-treet.html", {'form': form})


@login_required
def treet_details(request, treet_id):
    try:
        tr = Treet.objects.get(id=treet_id)
        return render(request, "market/treet-details.html", {'tr': tr})
    except Treet.DoesNotExist:
        raise Http404()
