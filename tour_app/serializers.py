from rest_framework import serializers
from django.utils import timezone

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