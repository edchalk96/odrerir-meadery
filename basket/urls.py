from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_basket, name="basket"),
    path("add/<item_id>/", views.add_to_basket, name="add_to_basket"),
]