from .models import Registration
from django.forms import ModelForm, TextInput


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = [
            'name',
            'email',
            'password'
        ]

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }



















