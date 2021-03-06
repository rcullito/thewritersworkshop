from django.shortcuts import render
from django.http import HttpResponse
from nltk.corpus import wordnet as wn
from .models import Greeting
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import WordForm
import nltk
nltk.download()

def index(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            searchword =  form.cleaned_data.get('your_word')
            possiblesynsets = wn.synsets(searchword)
            searchWordDefinitions = [synset.definition() for synset in possiblesynsets]

    else:
        form = WordForm()
        searchWordDefinitions = []

    return render(request, 'index.html', {'form': form, 'definitions': searchWordDefinitions })



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
