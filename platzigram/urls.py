from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World !')

urlpatterns = [

    path('helloworld/', hello_world)
    #path('admin/', admin.site.urls),
]
