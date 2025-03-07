# from django.core.mail import send_mail
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Banner, Service, Doctor, ContactSubmission, Blog
# from rest_framework.views import APIView
# from rest_framework import status
# from .serializers import ContactSubmissionSerializer

# @api_view(['GET'])
# def get_banner(request):
#     banners = Banner.objects.all()
#     data = [{"image": request.build_absolute_uri(banner.image.url), "caption": banner.caption} for banner in banners]
#     return Response(data)

# @api_view(['GET'])
# def get_services(request):
#     services = Service.objects.all()
#     data = [{"title": service.title, "description": service.description, "icon": service.icon, "details":service.details, "path": service.path } for service in services]
#     return Response(data)

# @api_view(['GET'])
# def get_blogs(request):
#     blogs = Blog.objects.all()
#     data = [{"title": blog.title,"slug":blog.slug, "content": blog.content, "published_date":blog.published_date, "image": request.build_absolute_uri(blog.image.url)} for blog in blogs]
#     return Response(data)


# # views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Doctor
# from .serializers import DoctorSerializer

# @api_view(['GET'])
# def get_doctors(request):
#     doctors = Doctor.objects.all()
#     serializer = DoctorSerializer(doctors, many=True, context={'request': request})
#     return Response(serializer.data)


# class ContactSubmissionAPIView(APIView):
#     def get(self, request):
#         submissions = ContactSubmission.objects.all()
#         serializer = ContactSubmissionSerializer(submissions, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ContactSubmissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ContactChoicesAPIView(APIView):
#     def get(self, request):
#         choices = [
#             {"value": choice[0], "label": choice[1]}
#             for choice in ContactSubmission.ChoiceOptions.choices
#         ]
#         return Response(choices, status=200)

# # 



from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Banner, Service, Doctor, ContactSubmission, Blog
from .serializers import ContactSubmissionSerializer, DoctorSerializer


@api_view(['GET'])
def get_banner(request):
    banners = Banner.objects.all()
    data = [
        {"image": request.build_absolute_uri(banner.image.url), "caption": banner.caption}
        for banner in banners
    ]
    return Response(data)


@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    data = [
        {
            "title": service.title,
            "description": service.description,
            "icon": service.icon,
            "details": service.details,
            "path": service.path,
        }
        for service in services
    ]
    return Response(data)


@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    data = [
        {
            "title": blog.title,
            "slug": blog.slug,
            "content": blog.content,
            "published_date": blog.published_date,
            "image": request.build_absolute_uri(blog.image.url),
        }
        for blog in blogs
    ]
    return Response(data)


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
