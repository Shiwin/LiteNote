from django.http.response import HttpResponseRedirect
from lite_note.models import Note

__author__ = 'Ivan'


def make_public_note(requst,id):
    note = Note.objects.get(pk=id)
    note.make_public()
    return HttpResponseRedirect('/')

def make_private_note(requst,id):
    note = Note.objects.get(pk=id)
    note.make_private()
    return HttpResponseRedirect('/')

def make_favorite_note(requst,id):
    note = Note.objects.get(pk=id)
    note.make_favorite()
    return HttpResponseRedirect('/')

def make_usual_note(requst,id):
    note = Note.objects.get(pk=id)
    note.make_usual()
    return HttpResponseRedirect('/')

def delet_note(requst,id):
    Note.objects.get(pk=id).delete()
    return HttpResponseRedirect('/')