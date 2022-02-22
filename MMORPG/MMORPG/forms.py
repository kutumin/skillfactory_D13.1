from django.forms import ModelForm
from .models import Category, Post
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['id', 'post_author', 'post_type', 'category','article_text',]

class SubscriberForm(forms.Form):
    email = forms.EmailField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), initial='detective')
    class Meta:
        fields = ['email',]