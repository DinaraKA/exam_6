from django import forms
from django.forms import widgets


class EntryForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='ФИО')
    email = forms.EmailField(required=True, label='Почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст',widget=widgets.Textarea)





