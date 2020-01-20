from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import FormView ,ListView, TemplateView
from .forms import ContactForm
from blog.models import Post


class HomeView(FormView,TemplateView):
    form_class = ContactForm
    template_name = 'welcome/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        featured = Post.published.filter(featured=True)
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['featured'] = featured
        return context
        
class AboutView(TemplateView):
    template_name = 'about_us/about.html'

    def get_context_data(self, **kwargs):
        latest = Post.published.order_by('-publish')[0:3]
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['latest'] = latest
        return context

class ServiceView(TemplateView):
    template_name = 'what_we_do/service.html'


class ProjectView(TemplateView):
    template_name = 'completed_projects/projects.html'

class ContactUsView(TemplateView):
    template_name = 'contact_us/contact_us.html'

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'form/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ContactView, self).form_valid(form)
