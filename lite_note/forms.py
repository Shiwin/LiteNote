from django.shortcuts import render_to_response
import lite_note

__author__ = 'Ivan'
from lite_note import models
from django import forms


class NoteForm(forms.ModelForm):

    class Meta:
        model = models.Note
        fields = ('title', 'category', 'note', )

