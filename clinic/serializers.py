from rest_framework import serializers
from .models import Service, Doctor, Blog ,Banner, ContactSubmission

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'

    def validate_choice(self, value):
        valid_choices = [choice[0] for choice in ContactSubmission.ChoiceOptions.choices]
        if value not in valid_choices:
            raise serializers.ValidationError("Invalid choice selected.")
        return value
