from django import forms

class WordForm(forms.Form):
    your_word = forms.CharField(label='Word', max_length=100)
