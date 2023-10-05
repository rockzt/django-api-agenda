from rest_framework import serializers
from django.contrib.auth.models import User  # Used on UserModelSerializer
from . import models


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = ("username", "password", "email")

    # Overwriting create method to store password encrypted instead plain text
    def create(self, validated_data):
        #Receiven data from serializer and then execute create_user
        return self.Meta.model.objects.create_user(**validated_data)


class ContactModelSerializer(serializers.ModelSerializer):
    """Contact Model Serializer"""
    class Meta:
        model = models.Contact
        fields = ("first_name","middle_name","email","phone","mobile", "user")