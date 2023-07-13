from django.contrib import admin

# Register your models here.
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'content', 'image',)
    # search_fields = ('name', 'description',)
    list_filter = ('created_at',)