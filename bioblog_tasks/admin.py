from django.contrib import admin
from .models import User, Comment, BlogPost

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(BlogPost)
# Register your models here.
