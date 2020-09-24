from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMessage
from django.conf import settings
from requests.exceptions import HTTPError
from rest_framework.authtoken.models import Token
from rest_framework.relations import RelatedField
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField
from django.template import loader
from apps.users.serializers import RetrieveUserSerializer
from .models import *
from apps.users.models import User
from apps.serializers import *


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ('id',)


class SchoolViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id',)


class StudentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('id',)


class TeacherViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
