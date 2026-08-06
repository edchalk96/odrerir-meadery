from . import views
from django.urls import path

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("<int:product_id>/add_review/", views.add_review, name="add_review"),
    path('add/', views.add_product, name='add_product'),
    path('delete-product/<int:product_id>/',
         views.delete_product, name='delete_product'),
]
