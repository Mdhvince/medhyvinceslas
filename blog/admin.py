from django.contrib import admin

from .models import BlogPost, Review

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Review)