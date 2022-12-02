from django.shortcuts import render, redirect
from .models import Offer
from .forms import OfferForm
# Create your views here.


def add_offer(request):
    error = ''
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            # return redirect('offer')
            # return render(request, 'add_offer/offers_adding.html', {'form': form, 'img_obj': img_obj })
            return redirect('catalog')
        else:
            error = 'Форма была неверной'

    form = OfferForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'add_offer/offers_adding.html', {'form': form})






















