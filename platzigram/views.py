""" Platzigram Views. """

#Django
import pdb
from django.http import HttpResponse

#utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hi, the current server time is {now}'.format(now=str(now)))


def sort_integers(request):
    """Return a JSON response with sorted ints """
    numbers = [int(i) for i in request.GET['numbers'].split(',')] 
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'mesage': 'Integers sorted succesfully.'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, age):
    """ Return a greeting """
    if age < 12:
        message = 'Sorry {}, you aren\'t allowed here'.format(name)
    else:
        message = 'Hello {} !!! Welcome to Platzigram'.format(name)

    return HttpResponse(message)