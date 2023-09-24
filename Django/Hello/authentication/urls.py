# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('authentication.urls')),
#     path('', views.index),
#     path('contact/', views.contact, name='contact'),
#     path('about/', views.about, name='about'),
#     path('login/', views.login, name='login'),
#     path('signup/', views.signup, name='signup'),

# ]
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
