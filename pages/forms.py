from django import forms
from posts.models import Publica
class CreatePost(forms.ModelForm):
    class Meta:
        model=Publica
        fields=['image','title','content']
    def save(commit=True):
        if commit:
            Publica.save()
