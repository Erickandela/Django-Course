""" Platzigram URLs module. """
from django.urls import path
from platzigram import views



urlpatterns = [

    path('helloworld/', views.hello_world),
    path('sorted/', views.sort_integers),
    path('hi/<str:name>/<int:age>', views.say_hi)
    #path('admin/', admin.site.urls),
]
