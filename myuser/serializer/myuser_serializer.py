from rest_framework import serializers
from myuser.models import MyUser

__author__ = 'challa'


class MyUserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')

    class Meta:
        model = MyUser
        fields = ('username', 'firstName', 'lastName', 'email', 'address', 'phone', 'groups')