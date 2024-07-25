"""
URL configuration for agl_case_generator project.

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
from django.views.generic.base import RedirectView 
from endoscopy_anticoagulation.urls import urlpatterns as endoscopy_anticoagulation_urls


urlpatterns = [
    # temporarily "/" should redirect to "/endoscopy_anticoagulation/"
    # ADD CODE HERE
    path('', RedirectView.as_view(url='/endoscopy_anticoagulation/', permanent=False)),
    path('admin/', admin.site.urls),
    path('endoscopy_anticoagulation/', include(endoscopy_anticoagulation_urls)),
]
