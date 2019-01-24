from django.contrib import admin
from .models import contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Email','contact_at')
    list_display_links = ('id','Name','Email')
    search_fields = ('Name','Email','Message','subject')
    list_per_page = 25
admin.site.register(contact, ContactAdmin)