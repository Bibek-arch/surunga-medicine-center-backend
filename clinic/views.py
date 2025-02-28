from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Banner, Service, Doctor, ContactSubmission, Blog
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ContactSubmissionSerializer

@api_view(['GET'])
def get_banner(request):
    banners = Banner.objects.all()
    data = [{"image": request.build_absolute_uri(banner.image.url), "caption": banner.caption} for banner in banners]
    return Response(data)

@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    data = [{"title": service.title, "description": service.description, "icon": service.icon, "details":service.details, "path": service.path } for service in services]
    return Response(data)
from django.http import JsonResponse
from .models import Blog

def blog_detail(request, pk):
    blog_post = get_object_or_404(Blog, pk=pk)
    return render(request, 'templates/blog/blog_detail.html', {'blog_post': blog_post})

@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    data = [{"title": blog.title,"slug":blog.slug,"content": blog.content, "published_date":blog.published_date, "image": request.build_absolute_uri(blog.image.url)} for blog in blogs]
    return Response(data)

# @api_view(['GET'])
# def get_doctors(request):
#     doctors = Doctor.objects.all()
#     data = [{"name": doctor.name, "specialty": doctor.specialty, "days":doctor.days, "time":doctor.time, "details": doctor.details, "image": request.build_absolute_uri(doctor.image.url)} for doctor in doctors]
#     return Response(data)

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True, context={'request': request})
    return Response(serializer.data)


class ContactSubmissionAPIView(APIView):
    def get(self, request):
        submissions = ContactSubmission.objects.all()
        serializer = ContactSubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ContactChoicesAPIView(APIView):
    def get(self, request):
        choices = [
            {"value": choice[0], "label": choice[1]}
            for choice in ContactSubmission.ChoiceOptions.choices
        ]
        return Response(choices, status=200)

# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from .models import Blog

# def get_blog_metadata(request, post_id):
#     post = get_object_or_404(Blog, id=post_id)
#     return JsonResponse({
#         "title": post.title,
#         "content": post.content,
#         "image": request.build_absolute_uri(post.image.url),
#         "url": f"https://surungamedicine.com.np/blog/{post.id}"
#     })
# from django.shortcuts import render, get_object_or_404
# from .models import Blog # Assuming you have a BlogPost model

# def blog_post_detail(request, slug):
#     # Fetch the blog post using the slug
#     blog_post = get_object_or_404(Blog, slug=slug)

#     # Prepare meta tags for the blog post
#     meta_tags = {
#         "title": blog_post.title,
#         "description": blog_post.content[:150],  # First 150 characters of the content
#         "image": blog_post.image.url if blog_post.image else "/static/placeholder.svg",
#         "url": request.build_absolute_uri(),
#     }

#     # Render the index.html template with the meta tags
#     return render(request, "index.html", {"meta_tags": meta_tags})

from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_detail(request, pk):
    blog_post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Banner, Doctor, Blog
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Blog

def blog_meta_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    meta_tags = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{blog.title}</title>
        <meta property="og:title" content="{blog.title}" />
        <meta property="og:description" content="{blog.content[:150]}" />
        <meta property="og:image" content="{blog.image.url if blog.image else 'https://surungamedicine.com.np/default-image.jpg'}" />
        <meta property="og:url" content="https://surungamedicine.com.np/blog/{blog.slug}" />
        <meta property="og:type" content="article" />
        <script>
            window.location.href = "https://surungamedicine.com.np/blog/{blog.slug}";
        </script>
    </head>
    <body>
    </body>
    </html>
    """
    
    return HttpResponse(meta_tags)

# @api_view(['GET'])
# def get_banner(request):
#     banners = Banner.objects.all()
#     data = [{"image": banner.image.url if banner.image else "", "caption": banner.caption} for banner in banners]
#     return Response(data)
# import cloudinary.uploader
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Blog
# from .serializers import BlogSerializer
# from django.conf import settings

# @api_view(['GET'])
# def get_blogs(request):
#     blogs = Blog.objects.all()
#     serializer = BlogSerializer(blogs, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def create_blog(request):
#     serializer = BlogSerializer(data=request.data)
#     if serializer.is_valid():
#         # Handle image upload to Cloudinary
#         image = request.FILES.get('image')
#         if image:
#             # Upload image to Cloudinary
#             result = cloudinary.uploader.upload(image)
#             # Set the image URL from Cloudinary to the Blog model
#             serializer.validated_data['image'] = result['secure_url']
        
#         # Save the blog post with the image URL
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_doctors(request):
#     doctors = Doctor.objects.all()
#     data = [{"name": doctor.name, "specialty": doctor.specialty, "days": doctor.days, "time": doctor.time, "details": doctor.details, "image": doctor.image.url} for doctor in doctors]
#     return Response(data)

