from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView
from .models import Post, Category
from .forms import CommentForm
from pages.forms import SubscribeForm, ContactForm

#### POST VIEWS MAIN  ######

class PostListView(ListView):
    model = Post
    model = Category
    template_name = 'blog/list.html'
    context_object_name = 'post'
    paginate_by = 1
    success_url = 'post-list'
    success_message = "You are now a subscriber Thank you"
    
   
    def post(self, request, *args, **kwargs):
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
    
    

    def get_context_data(self, **kwargs):
        post = Post.published.all()[0:6]
        
        featured = Post.published.filter(featured=True)
        latest = Post.published.order_by('-publish')[0:4]
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        context['category'] = Category.objects.filter()
        context['post'] = post
        context['featured'] = featured
        context['latest'] = latest
        return context

### POST DETAIL VIEW ### 

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        comment_form = CommentForm
        new_comment = None
        context = super().get_context_data(**kwargs)
        context['new_comment'] = new_comment
        context['comment_form'] = comment_form
        return context