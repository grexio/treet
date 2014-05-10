from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import Http404

from market.models import Treet, TreetPurchase, TreetReview
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


@login_required
def purchase_treet(request, treet_id):
    try:
        tr = Treet.objects.get(id=treet_id)
    except Treet.DoesNotExist:
        raise Http404
    tp = TreetPurchase.objects.create(treet=tr,
                       purchaser=request.user,
                       seller=tr.user,
                       state='PEND')
    messages.success(request, 'Treat has been successfully purchased.')
    return redirect(reverse("treet-details", args=(tr.id,)))


@login_required
def purchased_treets(request):
    state = request.GET.get('state')
    if state not in dict(TreetPurchase.STATES):
        state = 'PEND'
    pts = TreetPurchase.objects.filter(purchaser=request.user, state=state)
    return render(request, "market/purchased-treets.html",
                  {
                      'pts': pts,
                      'states': TreetPurchase.STATES,
                      'active_state': state,
                  })


@login_required
def sold_treets(request):
    state = request.GET.get('state')
    if state not in dict(TreetPurchase.STATES):
        state = 'PEND'
    pts = TreetPurchase.objects.filter(seller=request.user, state=state)
    return render(request, "market/sold-treets.html",
                  {
                      'pts': pts,
                      'states': TreetPurchase.STATES,
                      'active_state': state,
                  })
