__author__ = 'Ivan'
from django import forms
from lite_note import models



class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = models.Note
        fields = ('title', 'category', 'note', )

class NoteForm(forms.ModelForm):

    class Meta:
        model = models.Note
        exclude = ('id',)