from rest_framework import serializers
from app.task import (create_user_with_validated_data,
                      create_article_with_validated_data,)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(
        max_length=200, style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    def create(self, data):
        return create_user_with_validated_data(data)


class UserSerializerDetail(UserSerializer):

    def get_fields(self):
        """Remove unwanted fields"""
        excluded_fields = ('username', 'email')
        fields = super().get_fields()

        for field in excluded_fields:
            fields.pop(field)
        return fields

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.set_password(data.get('password'))
        instance.save()
        return instance


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    detail = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return create_article_with_validated_data(validated_data)
