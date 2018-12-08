#! python3
# Author: George Gao, gaojz017@163.com

from django import forms
from .models import Comment
import markdown
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
