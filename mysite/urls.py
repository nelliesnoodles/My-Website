"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('jstests.urls')),
    path('', include('WIWA.urls')),
    path('', include('StatsClass.urls')),
    path('', include('MontySlackBot.urls')),
    path('blog/', include('blog.urls')),
    path('language', include('blog.urls')),
    path('jstests/', include('jstests.urls')),
    path('WIWA', include('WIWA.urls')),
    path('PreWork2019', include('PreWork2019.urls')),
    path('StatsClass', include('StatsClass.urls')),
    path('MontySlackBot', include('MontySlackBot.urls')),
   ]