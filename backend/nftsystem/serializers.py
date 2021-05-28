from . import models
from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class MetadataSerializer(serializers.ModelSerializer):
    token = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset = models.BaseToken.objects.all())
    title = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    content = serializers.CharField(required=False)

    def create(self, validated_data):
        return models.Metadata.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.token = validated_data.get('token', instance.token)
        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        return instance

    class Meta:
        model = models.Metadata
        fields = ['token', 'title', 'type', 'name', 'description', 'content']
        
class BaseTokenSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset = models.CustomUser.objects.all())
    tokenId = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    metadata = MetadataSerializer(required=False)

    def create(self, validated_data):
        return models.BaseToken.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.tokenId = validated_data.get('tokenId', instance.tokenId)
        instance.address = validated_data.get('address', instance.address)
        return instance

    class Meta:
        model = models.BaseToken
        fields = ['pk', 'user', 'tokenId', 'address', 'metadata']

