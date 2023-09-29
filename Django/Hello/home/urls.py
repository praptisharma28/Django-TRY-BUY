from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
)

    
