from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        labels = {
            'name': 'İsim',
            'body': 'Yorum',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsminizi girin'}),
            'body': forms.Textarea(attrs={'placeholder': 'Yorumunuzu girin'}),
        }
