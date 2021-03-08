""" Post forms. """

#Django
from django import forms
from django.forms.forms import Form

#Models
from posts.models import Posts

class PostForm(forms.ModelForm):
    """ Post model form. """

    class Meta:
        """ Form settings """
        model = Posts
        fields = ('user', 'profile', 'title', 'photo')