from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_room, name='book_room'),
    path('registration_list', views.registration_list, name='registration_list'),
    path('registration_detail/<int:pk>/', views.registration_detail, name='registration_detail'),
]
