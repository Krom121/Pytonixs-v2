from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView
from .models import Post
from .forms import CommentForm
from pages.forms import SubscribeForm, ContactForm

#### POST VIEWS MAIN  ######

class PostListView(ListView):
    model = Post
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



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        form = SubscribeForm
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))
