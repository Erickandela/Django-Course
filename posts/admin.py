from django.contrib import admin
from django.contrib.auth.models import User
from posts.models import Posts

# Register your models here.

@admin.register(Posts)
class PostModel(admin.ModelAdmin) :
    """ Posts Model. """
    list_display=('pk','user', 'photo')
    list_display_links=('pk', 'user')
    list_editable= ('photo',)
    list_filter=('created', 'modified')

admin.site.unregister(User)
admin.site.register(User)