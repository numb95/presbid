from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import Context
from django.template.loader import get_template
from django.contrib import auth

from presbid.accounts import models
from presbid.accounts import forms

def register (request):
    if request.method == 'POST':
        form = forms.CustomRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    args = {}
    args.update(csrf(request))
    args['form'] = forms.CustomRegistration()
    return render(request, 'register.html', dict(args, **{'PageTile': " - Register"}))


