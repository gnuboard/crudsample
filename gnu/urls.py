from django.urls import path
from . import views

app_name = 'gnu'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('read/<int:article_id>', views.read, name='read'),
    path('form/', views.form, name='form'),
    path('edit/<int:article_id>', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('delete/<int:article_id>', views.delete, name='delete'),
]