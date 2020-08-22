"""appeals_novoross URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('apeals/<str:apeals_uid>', views.apeals_view, name='apeals_view'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('form/', include('dashboard.urls')),
    path('api/', include('api.urls')),
    
    
]
