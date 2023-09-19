from django import forms
from .models import Post

class LikeForm(forms.Form):
    action = forms.ChoiceField(choices=[('add', 'Adicionar Like'), ('remove', 'Remover Like')])


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
