from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    caption = models.TextField(max_length=300)

    def __str__(self):
        return self.caption

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class Doctor(models.Model):
    image = models.ImageField(upload_to='doctors/')
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    days = models.CharField(max_length=50,default='Monday - Friday')
    time = models.CharField(max_length=50,default='9:00 AM - 5:00 PM')
    details = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    published_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.title

# models.py

from django.db import models

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
