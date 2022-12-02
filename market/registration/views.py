from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm

# Create your views here.


# def registration(request):
#     regs = Registration.objects.all()
#     return render(request, "")


def create_registration(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        else:
            error = 'Форма была неверной'

    form = RegistrationForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/registration.html', data)















