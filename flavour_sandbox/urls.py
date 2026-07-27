from . import views
from django.urls import path

urlpatterns = [
    path("", views.sandbox_list, name="sandbox"),
    path("<int:idea_id>/", views.idea_detail, name="idea_detail"),
    path("like/<int:pk>/", views.like_idea, name="like_idea"),
]