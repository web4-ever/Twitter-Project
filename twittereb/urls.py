from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('post/', views.post, name = 'post'),
    path('detail/<int:id>/', views.detail, name = 'detail'),
    path('reply/<int:id>', views.reply, name = 'reply'),
    ]