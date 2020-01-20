from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import FormView ,ListView, TemplateView
from .forms import ContactForm
from blog.models import Post


class HomeView(FormView,TemplateView):
    form_class = ContactForm
    template_name = 'page/welcome/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        featured = Post.published.filter(featured=True)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        context['featured'] = featured
        return context
        
class AboutView(TemplateView):
    template_name = 'page/about_us/about.html'

    def get_context_data(self, **kwargs):
        latest = Post.published.order_by('-publish')[0:3]
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['latest'] = latest
        return context

class ServiceView(TemplateView):
    template_name = 'page/what_we_do/service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Services'
        return context

class ProjectView(TemplateView):
    template_name = 'page/completed_projects/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our Work'
        return context

class ContactUsView(TemplateView):
    template_name = 'page/contact_us/contact_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        return context

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'form/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ContactView, self).form_valid(form)
