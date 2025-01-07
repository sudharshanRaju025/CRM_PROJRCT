from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        

    def validate_username(self,value):
        
        if not value[0].isupper():
            raise serializers.ValidationError("first letter must be uppercase.")
        if not value.isalpha():
            raise serializers.ValidationError("username must be letters")
        if len(value)<3:
            raise serializers.ValidationError("username will be greater than 3 characters.")
        return value
    
    def validate_password(self,value):

        if not value[0].isupper():
            raise serializers.ValidationError("password first letter must be uppercase.")
        if len(value)<6:
            raise serializers.ValidationError("password must contain 6 characters")
        if User.objects.filter(password=value).exists():
            raise serializers.ValidationError("This password has been already been used.")
        return value

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
