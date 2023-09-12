from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile.models import Profile


class UserRegisterSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(label='Емейл')
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password1']
        return User.objects.create_user(email=email, username=username, password=password)


class ProfileRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user',)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude=('user',)
