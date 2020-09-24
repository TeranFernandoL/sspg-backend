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
from apps.faculties.serializers import *


class PeriodAcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodAcademic
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectViewSerializer(serializers.ModelSerializer):
    student_1 = StudentViewSerializer()
    student_2 = StudentViewSerializer()
    student_3 = StudentViewSerializer()
    adviser = TeacherViewSerializer()
    jury_1 = TeacherViewSerializer()
    jury_2 = TeacherViewSerializer()
    jury_3 = TeacherViewSerializer()
    period_academic = PeriodAcademic()

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id',)
