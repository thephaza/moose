from django.contrib import admin
from .models import Post, Tag, Comment, Contact


# Register your models here.

class Contactadmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email',
                    'subject', 'message', 'is_solved')
    list_display_links = ('id', 'full_name', 'email')


class Postadmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'tag', 'is_published', 'created_at')
    list_display_links = ('id', 'author_name')


admin.site.register(Post, Postadmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Contact, Contactadmin)
