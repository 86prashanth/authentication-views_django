from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required,name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name='cls/profile.html'
    
class AboutTemplateView(TemplateView):
    template_name='cls/about.html'
    