from django.urls import path
from . import views

urlpatterns = [
    ##item
    path('', views.item_list, name='item_list'),
    path('item/new', views.item_create, name='item_create'),
    path('item/edit/<int:pk>/', views.item_update, name='item_update'),
    path('item/delete/<int:pk>/', views.item_delete, name='item_delete'),
    ##categoria
    path('categoria/', views.categoria_list, name='categoria_list'),
    path('categoria/new/', views.categoria_create, name='categoria_create'),
    path('categoria/edit/<int:pk>/', views.categoria_update, name='categoria_update'),
    path('categoria/delete/<int:pk>/', views.categoria_delete, name='categoria_delete'),
    path('autor/', views.autor_list, name='autor_list'),
    path('autor/new/', views.autor_create, name='autor_create'),
    path('autor/edit/<int:pk>/', views.autor_update, name='autor_update'),
    path('autor/delete/<int:pk>/', views.autor_delete, name='autor_delete'),
]
