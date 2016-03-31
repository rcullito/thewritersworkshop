from django.shortcuts import render
from django.http import HttpResponse
from nltk.corpus import wordnet as wn
from .models import Greeting

from django.shortcuts import render
from django.http import HttpResponseRedirect

import logging
logger = logging.getLogger(__name__)

from .forms import WordForm

def index(request):

    # create a form instance and populate it with data from the request:
    form = WordForm(request.GET)
    # check whether it's valid:
    print 'hey man'
    # if form.is_valid():
    #     # process the data in form.cleaned_data as required
    #     ### inspect the form
    #     print form

    return render(request, 'index.html', {'form': form, 'wordnet': {} })



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
