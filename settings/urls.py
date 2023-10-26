"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('home/', views.home, name='home'),
    path('visitedcities/', views.visited_cities, name='visitedcities'),
    path('accounts/', include('allauth.urls')),
    path('map/', views.user_map, name='map'),
    path('newvisitedcity/', views.new_visited_city, name='newvisitedcity'),
    path('deletevisitedcity/<int:id>', views.delete_visited_city, name='deletevisitedcity')
]
