#! coding:utf-8
from django.forms import widgets
from rest_framework import serializers
from user_auth.models import User_extra,Corporation_profile,Employee_profile
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='password',widget=widgets.PasswordInput())
    confirmpassword = serializers.CharField(widget=widgets.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','confirmpassword')

    def validate_repeatpassword(self,attrs,source):
        repeatpassword = attrs.get('confirmpassword')
        password = attrs.get('password')
        if repeatpassword != password:
            raise serializers.ValidationError("password confirm error")
        return attrs

