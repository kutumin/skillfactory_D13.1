from django.forms import ModelForm
from .models import Category, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['id','category','article_text', 'image', 'video']

class SubscriberForm(forms.Form):
    email = forms.EmailField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), initial='detective')
    class Meta:
        fields = ['email',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','active')
