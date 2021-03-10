""" Posts urls. """

#Django
from django.urls import path

#Views
from posts import views


urlpatterns = [
    #Magnament

    path(
        route = '',
        view = views.PostsFeedView.as_view(), 
        name='feed'
        ),
    path(
        route ='posts/new', 
        view=views.create_post, 
        name='create'
        ),

    #Posts
    path(
        route = 'posts/<int:post_id>',
        view=views.PostDetailView.as_view(),
        name = 'post_detail'
    )

]
