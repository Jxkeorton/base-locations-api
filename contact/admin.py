from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
