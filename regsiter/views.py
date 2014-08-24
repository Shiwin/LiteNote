import json
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse


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
    return render_to_response('registration/registration_form.html', args)

def request_login(request):
    if request.method == 'POST':
        requser = request.POST['username']
        reqpass = request.POST['password']
        user = authenticate(username=requser, password=reqpass)
        response_data = {}
        if user is not None:
            if user.is_active:
                login(request, user)
                # Return a success message
                response_data['result'] = 'success'
                response_data['message'] = 'Has loged in'
                response_data['fullname'] = user.get_full_name()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                # Return a 'disabled account' error message
                response_data['result'] = 'disabled'
                response_data['message'] = 'this user is disabled'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            # Return an 'invalid login' error message.
            response_data['result'] = 'failed'
            response_data['message'] = 'invalid login'
            return HttpResponse(json.dumps(response_data), content_type="application/json")