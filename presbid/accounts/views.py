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


def login(request):
    invalid_html=""
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST.get('username',''), password = request.POST.get('password',''))
        if user is not None:
            auth,login(request,user)
            return (HttpResponseRedirect('/'))
        else:
            invalid_html = get_template('invalid.html')
        args = {}
        args.update(csrf(request))
        return render(request, 'login.html', dict(c, **{'PageTitle' : " - Login", 'invalid.html' : invalid_html}))