from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password':{'write_only':True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_staff']
        extra_kwargs = {'password':{'write_only':True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        Token.objects.create(user=user)
        return user