""" Posts views. """

#Django
#from django.http import HttpResponse
from django.shortcuts import render


#Utilities
from datetime import date, datetime


posts = [
    {   
        'title': 'Mont Blac',
        'user': {
            'name': 'Yessica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1036'
        },
        
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs') ,
        'photo': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'title': 'Via Láctea',
        'user':{
            'name': 'C Vander',
            'picture': 'https://picsum.photos/60/60/?image=903'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs') ,
        'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {   
        'title': 'Nuevo Auditorio',
        'user':{
            'name': 'Thepianartist',
            'picture': 'https://picsum.photos/60/60/?image=1076'
        },
        
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs') ,
        'photo': 'https://picsum.photos/200/200/?image=1076',
    }
]

# Create your views here.


def lists_posts(request):
    """ List existing posts. """
    return render (request, 'posts/feed.html', {'posts': posts })