from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( "name","email", "body")

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': "enter your first name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': "Email"}))
