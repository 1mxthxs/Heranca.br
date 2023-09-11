from django import forms

class LikeForm(forms.Form):
    action = forms.ChoiceField(choices=[('add', 'Adicionar Like'), ('remove', 'Remover Like')])
