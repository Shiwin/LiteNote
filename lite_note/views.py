from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lite_note import models, forms
from lite_note.models import Note


def home(request):
    notes = models.Note.objects.all().filter(author=request.user)
    return render(request, 'lite_note/index.html', {'notes': notes, })


@login_required(login_url='/login/')
def note(request, id):
    item = models.Note.objects.get(pk=id)
    return render(request, 'lite_note/note.html',
                  {'note': item, 'date': item.create_date})


@login_required(login_url='login/')
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
        return render(request, 'lite_note/note_form_create.html',args)