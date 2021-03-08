from django.contrib import admin
from django.contrib.auth.models import User
from posts.models import Posts

# Register your models here.

@admin.register(Posts)
class PostModel(admin.ModelAdmin) :
    """ Posts Model. """
    list_display = ('id', 'user', 'title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

admin.site.unregister(User)
admin.site.register(User)