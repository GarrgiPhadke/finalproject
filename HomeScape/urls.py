"""
URL configuration for HomeScape project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from index import views as main_views

from account.views import (
    registration_view,login_view,logout_view,account_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.index, name='index'),

    path('register/', registration_view, name ="register"),
    path('logout/', logout_view, name ="logout"),
    path('login/', login_view, name ="login"),
    path('account/', account_view, name ="account"),

    path('hub/',include('hub.urls')),
    path('cal/', include('cal.urls')), 
    path('review/',include('review.urls')),
    path('contact/',include('contact.urls')), 
    path('aboutus/',include('aboutus.urls')),
    path('myservice/',include('myservice.urls')),
    path('myservice/',include('booking.urls')),
    
   
]