from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import FormView ,ListView, TemplateView
from .models import NewClient
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
        
class AboutView(TemplateView):
    template_name = 'about_us/about.html'


class ServiceView(TemplateView):
    template_name = 'what_we_do/service.html'


class ProjectView(TemplateView):
    template_name = 'completed_projects/projects.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'form/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(ContactView, self).form_valid(form)
