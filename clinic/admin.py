
from django.contrib import admin
from .models import Banner, Service, Doctor, ContactSubmission,Blog

admin.site.site_header = "Surunga Medicine Center Admin"
admin.site.site_title = "Surunga Medicine Center Admin Panel"
admin.site.index_title = "Welcome to Surunga Medicine Center Admin Panel"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'image')
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'details', 'path')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty','days', 'time', 'details', 'image')
# admin.py
from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message', 'choice', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'phone_number','choice', 'message')
