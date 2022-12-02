from .models import Offer
from django import forms
from django.forms import ModelForm, TextInput, NumberInput, FileInput


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = [
            'name',
            'description',
            'price',
            'contacts',
            'image'
        ]

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'contacts': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваши контакты'
            }),
            'image': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Изображение'
            })
        }














