from django.contrib import admin
from portfolio_app.models import Project, ContactMessage

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'tech_stack', 'short_description', 'description')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('created_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'message')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
