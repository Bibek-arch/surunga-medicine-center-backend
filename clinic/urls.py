from django.urls import path
from .views import ContactSubmissionAPIView,ContactChoicesAPIView
from .views import get_banner, get_services, get_doctors, get_blogs
urlpatterns = [
    path('banners/', get_banner),
    path('services/', get_services),
    path('blogs/',get_blogs),
    path('doctors/', get_doctors),
    path('contact-submissions/', ContactSubmissionAPIView.as_view(), name='contact-submission'),
    path('contact-choices/', ContactChoicesAPIView.as_view(), name='contact-choices'),



]