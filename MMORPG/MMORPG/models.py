from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django import forms

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", 
                  "email", 
                  "password1", 
                  "password2", )

class Category(models.Model):
    TANKS = 'T'
    HILLS = 'H'
    DEALER = 'D'
    GILDMASTER = 'GM'
    QUESTGIVER = 'QG'
    SMITH = 'SM'
    LEATHERS = 'L'
    POISONMAKER = 'PM'
    SPELLMASTER = 'SM'

    POST_CATEGORY = [
        (TANKS, 'Tanks'),
        (HILLS, 'Hills'),
        (DEALER, 'Dealer'),
        (GILDMASTER, 'Gildmaster'),
        (QUESTGIVER, 'Questgiver'),
        (SMITH, 'Smith'),
        (LEATHERS, 'Leathers'),
        (POISONMAKER, 'Poisonmaker'),
        (SPELLMASTER, 'Spellmaster'),
    ]
    category_name = models.CharField(
        max_length=2,
        choices=POST_CATEGORY,
        default=None
    )
    def __str__(self):
        return f'{self.category_name}'

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Name")
    last_name = forms.CharField(label = "Surname")

    class Meta:
        model = User
        fields = ("username", 
                  "first_name", 
                  "last_name", 
                  "email", 
                  "password1", 
                  "password2", )
                  
    def save(self, request):
        user = super(BaseRegisterForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

class Author(models.Model):
    full_name = models.CharField(max_length = 255)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Post(models.Model):
    TANKS = 'T'
    HILLS = 'H'
    DEALER = 'D'
    GILDMASTER = 'GM'
    QUESTGIVER = 'QG'
    SMITH = 'SM'
    LEATHERS = 'L'
    POISONMAKER = 'PM'
    SPELLMASTER = 'SM'

    POST_CATEGORY = [
        (TANKS, 'Tanks'),
        (HILLS, 'Hills'),
        (DEALER, 'Dealer'),
        (GILDMASTER, 'Gildmaster'),
        (QUESTGIVER, 'Questgiver'),
        (SMITH, 'Smith'),
        (LEATHERS, 'Leathers'),
        (POISONMAKER, 'Poisonmaker'),
        (SPELLMASTER, 'Spellmaster'),
    ]
    post_author = models.OneToOneField(User,on_delete = models.CASCADE)
    post_date_created = models.DateField(auto_now_add = True)
    post_detailed_data_created = models.TimeField(auto_now_add = True)
    category = models.CharField(max_length=2, choices=POST_CATEGORY)
    head_of_post = models.CharField(max_length = 255)
    article_text = models.TextField()
    image = models.FileField(blank=True)
    video = models.FileField(blank=True)

    def __str__(self):
        return self.head_of_post

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.head_of_post

class PostVideo(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.post.head_of_post
