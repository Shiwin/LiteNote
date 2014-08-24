__author__ = 'Ivan'
from django import forms
from lite_note import models



class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = models.Note
        fields = ('title', 'category', 'note', )

class NoteForm(forms.ModelForm):
    is_favorite = forms.BooleanField()
    is_public = forms.BooleanField()

    class Meta:
        model = models.Note
        exclude = ('id',)