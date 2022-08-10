from django.contrib import admin
from .models import Post 


@admin.register(Post)                                                          # edited
class PostAdmin(admin.ModelAdmin):                                             # new
    list_display = ['title', 'slug', 'author', 'publish', 'status']            # new

