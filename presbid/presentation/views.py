from django.shortcuts import render
from presentation.models import Presentation

def preseantations_table(request):
    preseantations = []
    for pres in Presentation.objects.all():
        preseantations.append(pres)
    return render (request, 'index.html', {'preseantations' : preseantations})


