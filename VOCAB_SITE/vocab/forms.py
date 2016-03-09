from django import forms

class MyForm(forms.Form):
    first_input = forms.CharField(label='first input', max_length=100)
