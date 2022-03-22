from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Category, Post, Author, Comment
from .forms import PostForm, CommentForm
from .filters import PostFilter
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.template import RequestContext
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache import cache
import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

class PostSearch(LoginRequiredMixin, ListView):
    def get(self, request):
        author_id = request.user.id
        user_posts = Post.objects.filter(post_author=author_id)
        template = 'protect/protected_index.html'
        return render(request, template, {'user_posts':user_posts,'author': author_id})

class PostListNews(ListView):
    model = Post
    template_name ='blog.html' 
    context_object_name = 'all_posts_list'
    paginate_by = 1
    ordering = ['-id']

class PostAdd(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'add_post.html'
    context_object_name = 'all_posts_list'
    form_class = PostForm
    success_url = '/blog/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id).order_by('id')

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context
 

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
                form.instance.post_author=request.user
                form.save()
                return redirect("/blog/")
        return super().get(request, *args, **kwargs)

class PostDetail(DetailView):
    model = Post
    template_name = 'details_post.html' 
    context_object_name = 'object'
    queryset = Post.objects.all()
    
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args,**kwargs)

        comments_connected = Comment.objects.filter(
        post=self.get_object()).order_by('-created_on')
        data['comments'] = comments_connected
        data['comment_form'] = CommentForm( )

        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)

        return data

    new_comment = None

    def post(self, request, *args, **kwargs):
        new_comment = Comment(text=request.POST.get('text'), author = self.request.user, post=self.get_object())
        new_comment.save()
        article_text=new_comment.text
        article_author=new_comment.author
        created = datetime.datetime.now()
        post = self.get_object()
        post_text = post.article_text
        tuple = {
                'article_text':article_text,
                'article_author':article_author,
                'post_text':post_text}
        html_content = render_to_string('email_template.html', { 'context': article_text, 'article_author':article_author, 'article_text':article_text, 'article_date': created, 'post_text': post_text},)
        msg = EmailMultiAlternatives(
            subject='новый комментарий!',
            body=html_content,
            from_email='skillfactory88@mail.ru',
            to=[post.post_author.email,])
        msg.attach_alternative(html_content, "text/html")
        msg.send() 
        
        return self.get(self, request, *args, **kwargs)

class PostDetailEdit(DetailView):
    model = Post
    template_name = 'details_post.html' 
    context_object_name = 'object'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    permission_required = ('news.add_post',)
    template_name = 'add_post.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'delete_post.html'
    queryset = Post.objects.all()
    context_object_name = 'all_posts_list'
    success_url = '/blog/'

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    comment_author = comment.author
    comment_text = comment.text
    created_on = comment.created_on
    post_text = comment.post.article_text
    html_content = render_to_string('email_template_comment.html', {'comment_author':comment_author, 'comment_text':comment_text, 'created_on': created_on, 'post_text':post_text},)
    msg = EmailMultiAlternatives(
        subject='Ваш комментарий был одобрен',
            body=html_content,
            from_email='skillfactory88@mail.ru',
            to=[comment.author.email,])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)