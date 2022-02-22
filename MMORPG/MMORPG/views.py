from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Category, Post, Author
from .forms import PostForm
from .filters import PostFilter

class PostListNews(ListView):
    model = Post
    template_name ='blog.html' 
    context_object_name = 'all_posts_list'
    ordering = ['id']
    paginate_by = 1

class PostAdd(ListView):
    model = Post
    template_name = 'add_post.html'
    context_object_name = 'all_posts_list'
    paginate_by = 1
    form_class = PostForm
    success_url = '/blog/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['PostCategory'] = Category.objects.all()
        context['form'] = PostForm()
        return context
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('/blog/')
