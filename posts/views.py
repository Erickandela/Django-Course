""" Posts views. """

#Django
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView


#Forms
from posts.forms import PostForm

#Models
from posts.models import Posts


class PostDetailView(DetailView, LoginRequiredMixin):
    """ Post detail view """
    template_name= 'posts/detail.html'
    slug_field='id'
    slug_url_kwarg='post_id'
    queryset = Posts.objects.all()
    context_object_name='post'

# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts """
    template_name= 'posts/feed.html'
    model = Posts
    ordering = ('-created',)
    #paginate_by = 
    context_object_name = 'posts'


@login_required
def create_post(request):
    """ Create new post view """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request = request,
        template_name='posts/new.html',
        context= {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )