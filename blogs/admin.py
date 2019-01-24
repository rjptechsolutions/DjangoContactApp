from django.contrib import admin

from .models import BlogModel

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','created_at','author')
    list_display_links = ('id','title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title','body','author')
    list_per_page = 25
admin.site.register(BlogModel, BlogAdmin)