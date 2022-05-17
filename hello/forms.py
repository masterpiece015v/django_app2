from socket import fromshare
from django import forms

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')