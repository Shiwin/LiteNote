from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lite_note import models, forms
from lite_note.models import Note


def enter_anonymous_user(request):
    return render(request, 'lite_note/unknown_user.html')

def home(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('unknown/')
    else:
        notes = models.Note.objects.all().filter(author=request.user)
        return render(request, 'lite_note/index.html', {'notes': notes, })


@login_required(login_url='/unknown/')
def note(request, id):
    item = models.Note.objects.get(pk=id)
    if request.user == item.author:
        return render(request, 'lite_note/note.html',
                  {'note': item, 'date': item.create_date})
    else:
        return render(request, 'lite_note/no_access.html')


@login_required(login_url='/unknown/')
def create_note(request):
    args = {}
    args.update(csrf(request))
    form = forms.NoteForm(request.POST)
    if form.is_valid():
        note = form.save(commit=False)
        note.author = request.user
        note.save()
        return HttpResponseRedirect('/')
    else:
        form = forms.NoteForm()
        args['form'] = form
        return render(request, 'lite_note/note_create_form.html',args)



def new_home(request):
    """AJAX verison"""
    if request.user.is_anonymous():
        return render(request,'lite_note/new_index.html',{'notes':None,'user':request.user})
    else:
        notes = models.Note.objects.all().filter(author=request.user)
        return render(request, 'lite_note/new_index.html', {'notes': note,'user':request.user })