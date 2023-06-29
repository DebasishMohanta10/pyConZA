from django.contrib import admin
from .models import Category,Post
# Register your models here.

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

admin.site.register(Post,PostAdmin)