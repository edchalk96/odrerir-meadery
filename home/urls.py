from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path('contact-developer/', views.contact_developer, name='contact_developer'),
]