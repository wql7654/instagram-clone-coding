from django import forms
from .models import Instargram, Comment


class InstargramForm(forms.ModelForm):

    class Meta:
        model = Instargram
        fields = ('title', 'content','image',)
        # exclude = ('title',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('instargram', 'user',)



