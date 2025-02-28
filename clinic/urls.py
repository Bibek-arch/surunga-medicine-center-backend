from django.urls import path
from .views import ContactSubmissionAPIView,ContactChoicesAPIView
from .views import get_banner, get_services, get_doctors,blog_detail, get_blogs,blog_meta_view
urlpatterns = [
    path('banners/', get_banner),
    path('services/', get_services),
    path('blogs/',get_blogs),
    path('doctors/', get_doctors),
    path('contact-submissions/', ContactSubmissionAPIView.as_view(), name='contact-submission'),
    path('contact-choices/', ContactChoicesAPIView.as_view(), name='contact-choices'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('meta/blog/<slug:slug>/', blog_meta_view, name='blog-meta'),



]