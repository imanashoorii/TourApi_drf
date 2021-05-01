from rest_framework import serializers
from django.utils import timezone

from django.contrib.auth.models import User

from .models import Tour

class tourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
        read_only_fields = ('createdAt', 'updatedAt')

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.createdAt = timezone.now()
        obj.save()
        return obj

    def update(self, instance, validated_data):
        created_at = instance.createdAt

        obj = super().update(instance, validated_data)

        obj.createdAt = created_at
        obj.updatedAt = timezone.now()
        obj.save()
        return obj


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user