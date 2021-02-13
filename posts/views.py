""" Posts views. """

#Django
from django.http import HttpResponse


#Utilities
from datetime import date, datetime



posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yessica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs') ,
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Láctea',
        'user': 'C Vander',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs') ,
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Thepianartist',
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs') ,
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

# Create your views here.


def lists_posts(request):
    """ List existing posts. """
    content = []
    for post in posts:
        content.append(""" 
            <p><strong> {name} </strong></p>
            <p><small> {user} - <i>{timestamp}</i> </small></p>
            <figure><img src="{picture}" /></figure>
            """.format(**post))
    return HttpResponse('<br>'.join(content))