from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status, filters
from apps.faculties.serializers import *
from apps.faculties.models import *


class ListCreateSchoolAPIView(generics.ListCreateAPIView):
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = School.objects.all().order_by('id')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SchoolViewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = SchoolViewSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = SchoolViewSerializer(obj, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class RUDSchoolAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(School, id=self.kwargs['pk'])
        return obj


class ListCreateStudentAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Student.objects.all().order_by('id')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = StudentViewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = StudentViewSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = StudentViewSerializer(obj, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class ListStudentAvailableAPIView(generics.ListAPIView):
    serializer_class = StudentViewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Student.objects.filter(projects_student1=None, projects_student2=None)
        return queryset


class RUDStudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Student, id=self.kwargs['pk'])
        return obj


class ListCreateTeacherAPIView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Teacher.objects.all().order_by('id')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TeacherViewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = TeacherViewSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = TeacherViewSerializer(obj, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class RUDTeacherAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Teacher, id=self.kwargs['pk'])
        return obj


class ListTeacherAvailableAPIView(generics.ListAPIView):
    serializer_class = TeacherViewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Teacher.objects.filter(asesor=True)
        return queryset


