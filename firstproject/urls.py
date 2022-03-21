"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Hello World")

def helpPage(request):
    return HttpResponse("Help Page : <br/> <img src='https://media.giphy.com/media/3o7bu0zqQXqQQqQq2U/giphy.gif'/>")

def handle_not_found(request, exception):
    return HttpResponse("<center><h1 style='text-align:center'>Oh You Lost!</h1><br/><img style='width:auto;height:500px;text-align:center' src='https://i.pinimg.com/originals/90/fb/43/90fb4379e62ef4104a0bd58bae82fe35.gif' /><br/> <a href='/'>Go Home</a></center>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sayHello),
    path('help/',helpPage),
]

handler404 = handle_not_found
