from django.shortcuts import render
from presbid.presentation.models import Presentation
from presbid.presentation.forms import CommentForm

def preseantations_table(request):
    user = request.user
    preseantations = []
    for pres in Presentation.objects.all():
        preseantations.append(pres)
    return render (request, 'index.html', {'preseantations' : preseantations})


