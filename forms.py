from .models import Articles
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django.contrib.auth.models import User
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'surname', 'phone', 'email', 'password']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваше Ім\'я'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваше прізвище'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть номер телефону'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть вашу електронну пошту'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте надійний пароль'
            }),
        }
