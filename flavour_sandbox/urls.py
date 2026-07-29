from . import views
from django.urls import path

urlpatterns = [
    path("", views.sandbox_list, name="sandbox"),
    path("<int:idea_id>/", views.idea_detail, name="idea_detail"),
    path("like/<int:pk>/", views.like_idea, name="like_idea"),
    path("<int:idea_id>/edit_comment/<int:comment_id>", views.comment_edit, name='comment_edit'),
    path('<int:idea_id>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]