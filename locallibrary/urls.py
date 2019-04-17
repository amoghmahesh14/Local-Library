"""locallibrary URL Configuration

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
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
	path('catalog/',include('catalog.urls') ),

	#This is to redirect the website always to the catalog app when the path is just '' i.e., 127.0.0.1:8000
	path('', RedirectView.as_view(url='/catalog/', permanent=True)),

    #For User Authentication across the whole site
    path('accounts/', include('django.contrib.auth.urls')),

]

