from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content', 'rating']
        # exclude = ['post']
        labels = {
            'content': 'Comment',
            'name': 'Name',
            'rating': 'Rating'
        }