from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('', views.about),
    # path('', views.contact),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # path('contact.html/contact.html/', views.index, name='contact_contact'),
    # path('contact.html/about.html/', views.about, name='contact_about'),
    # path('about.html/index.html/', views.index, name='about_index'),
    # path('about.html/contact.html/', views.contact, name='about_contact'),

]

    
