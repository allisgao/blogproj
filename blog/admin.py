from django.contrib import admin
from .models import Post, Category, Tag

# 让后台显示更多的信息
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Post, PostAdmin)
# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)


