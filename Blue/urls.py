"""Blue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('sheets/', include('sheets.urls', namespace='sheets')),
    path('profiles/', include('django.contrib.auth.urls')),
    path('problems/', include('problems.urls', namespace='problems')),
    path('solve_activities/', include('solve_activities.urls', namespace='solve_activities')),
    path('admin/', admin.site.urls),


    path('announcement/', include("announcement.urls", namespace="announcement"), name="announcement"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
