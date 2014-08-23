from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def registration(request):
    args = {}
    args.update(csrf(request))
    form = UserCreationForm(request.POST)
    if form.is_valid():
        username, password = form.clean_username(), form.clean_password2()
        User.objects.create_user(username, password=password)
        auth_user = auth.authenticate(username=username, password=password)
        auth.login(request, auth_user)
        return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    args['form'] = form
    return render_to_response('html/../templates/registration/registration_form.html', args)
