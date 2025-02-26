from django.db import models
from cloudinary.models import CloudinaryField


class Banner(models.Model):
    image = CloudinaryField('image')
    caption = models.TextField(max_length=300)

    def __str__(self):
        return self.caption

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50,
        default='🩺', 
        help_text="Enter the icon "
    )
    details = models.TextField(max_length=200, default='')
    path = models.CharField(max_length=100, default='/services/')

    def __str__(self):
        return self.title

# class Doctor(models.Model):
#     image = CloudinaryField('image')
#     name = models.CharField(max_length=50)
#     specialty = models.CharField(max_length=100)
#     days = models.CharField(max_length=50,default='Monday - Friday')
#     time = models.CharField(max_length=50,default='9:00 AM - 5:00 PM')
#     details = models.TextField(max_length=200, default='')

#     def __str__(self):
#         return self.name
# models.py
from django.db import models
from cloudinary.models import CloudinaryField

class Doctor(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    qualification = models.CharField(max_length=255, default='')
    days = models.CharField(max_length=50, default='Monday - Friday')
    time = models.CharField(max_length=50, default='9:00 AM - 5:00 PM')
    services = models.TextField(default='')
    education = models.TextField(default='')
    details = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    published_date = models.DateField(auto_now_add=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

# models.py

from django.db import models
from cloudinary.models import CloudinaryField


class ContactSubmission(models.Model):
    class ChoiceOptions(models.TextChoices):
        GENERAL_INQUIRY = 'general_inquiry', 'General Inquiry'
        BOOK_APPOINTMENT = 'book_appointment', 'Book an Appointment'
        OTHER = 'other', 'Other'

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=300)
    choice = models.CharField(
        max_length=50,
        choices=ChoiceOptions.choices,
        default=ChoiceOptions.GENERAL_INQUIRY
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

# from django.db import models
# from cloudinary.models import CloudinaryField

# class Banner(models.Model):
#     image = CloudinaryField("image")  # Changed from ImageField
#     caption = models.TextField(max_length=300)

#     def __str__(self):
#         return self.caption

# class Doctor(models.Model):
#     image = CloudinaryField("image")  # Changed from ImageField
#     name = models.CharField(max_length=50)
#     specialty = models.CharField(max_length=100)
#     days = models.CharField(max_length=50, default='Monday - Friday')
#     time = models.CharField(max_length=50, default='9:00 AM - 5:00 PM')
#     details = models.TextField(max_length=200, default='')

#     def __str__(self):
#         return self.name
# from cloudinary_storage.storage import MediaCloudinaryStorage
# from cloudinary.models import CloudinaryField
# from django.db import models

# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     image = CloudinaryField()  # Upload to Cloudinary
#     published_date = models.DateTimeField(auto_now_add=True)




# # from django.db import models
# # import cloudinary
# # import cloudinary.uploader
# # import cloudinary.models

# # # Create your models here.
# # class Banner(models.Model):
# #     models.ImageField(upload_to='doctor_images/', null=True, blank=True)
# #     caption = models.TextField(max_length=300)

# #     def __str__(self):
# #         return self.caption

# # class Service(models.Model):
# #     id = models.AutoField(primary_key=True)
# #     title = models.CharField(max_length=50)
# #     description = models.CharField(max_length=100)
# #     icon = models.CharField(
# #         max_length=50,
# #         default='🩺', 
# #         help_text="Enter the icon "
# #     )
# #     details = models.TextField(max_length=200, default='')
# #     path = models.CharField(max_length=100, default='/services/')

# #     def __str__(self):
# #         return self.title

# # class Doctor(models.Model):
# #     models.ImageField(upload_to='doctor_images/', null=True, blank=True)
# #     name = models.CharField(max_length=50)
# #     specialty = models.CharField(max_length=100)
# #     days = models.CharField(max_length=50, default='Monday - Friday')
# #     time = models.CharField(max_length=50, default='9:00 AM - 5:00 PM')
# #     details = models.TextField(max_length=200, default='')

# #     def __str__(self):
# #         return self.name
    
# # class Blog(models.Model):
# #     title = models.CharField(max_length=100)
# #     content = models.TextField(max_length=500)
# #     published_date = models.DateField(auto_now_add=True)
# #     models.ImageField(upload_to='doctor_images/', null=True, blank=True)

# #     def __str__(self):
# #         return self.title

# # class ContactSubmission(models.Model):
# #     class ChoiceOptions(models.TextChoices):
# #         GENERAL_INQUIRY = 'general_inquiry', 'General Inquiry'
# #         BOOK_APPOINTMENT = 'book_appointment', 'Book an Appointment'
# #         OTHER = 'other', 'Other'

# #     name = models.CharField(max_length=100)
# #     phone_number = models.CharField(max_length=15)
# #     message = models.TextField(max_length=300)
# #     choice = models.CharField(
# #         max_length=50,
# #         choices=ChoiceOptions.choices,
# #         default=ChoiceOptions.GENERAL_INQUIRY
# #     )
# #     submitted_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"{self.name} - {self.phone_number}"
