from django.contrib import admin
from .models import *
# class PostAdmin(admin.ModelAdmin):
#     list_display = PostAdmin._meta.get_all_field_names()
#admin.site.register(Post, PostAdmin)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
