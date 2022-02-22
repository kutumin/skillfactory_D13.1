from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Category, Post, Author
from .forms import PostForm

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

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['PostCategory'] = PostCategory.objects.all()
        context['form'] = PostForm()
        return context
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid(): 
            form.save()
            article_text=form.cleaned_data['article_text']
            article_author=form.cleaned_data['post_author']
            created = datetime.datetime.now()
            print(form)
            tuple = {
                'article_text':article_text,
                'article_author':article_author,
            }
            print (tuple['article_text'])
            html_content = render_to_string('email_template.html', { 'context': form, 'article_author':article_author, 'article_text':article_text[:50], 'article_date': created})
            print (html_content)
            msg = EmailMultiAlternatives(
                subject='новая новость!',
                body=html_content,
                from_email='skillfactory88@mail.ru',
                to=['skillfactory88@mail.ru',])
            msg.attach_alternative(html_content, "text/html")
            msg.send() 
        return super().get(request, *args, **kwargs)