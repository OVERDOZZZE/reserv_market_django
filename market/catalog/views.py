from django.shortcuts import render


def show_catalog(request):
    offers = Offer.objects.all()
    return render(request, 'catalog/catalog.html', {'offers': offers})