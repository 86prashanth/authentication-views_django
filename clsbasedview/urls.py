from django.urls import path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('profile/',ProfileTemplateView.as_view(),name='profile'),
    path('about/',staff_member_required(AboutTemplateView.as_view()),name='about'),
]
