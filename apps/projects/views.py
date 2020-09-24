from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status, filters
from apps.projects.serializers import *
from apps.users.models import User


class ListCreateProyectoAPIView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        'name', 'student_1__first_name', 'student_1__last_name', 'student_1__code',
        'student_2__first_name', 'student_2__last_name', 'student_2__code', 'student_3__first_name',
        'student_3__last_name', 'student_3__code', 'jury_1__first_name', 'jury_1__last_name', 'jury_1__codigo',
        'jury_2__first_name', 'jury_2__last_name', 'jury_2__codigo', 'jury_3__first_name',
        'jury_3__last_name', 'jury_3__codigo', 'adviser__first_name',
        'adviser__last_name', 'adviser__codigo')

    def get_queryset(self):
        queryset = Project.objects.all().order_by('id')
        if self.request.query_params.get('type'):
            queryset = queryset.filter(type=self.request.query_params.get('type'))
        if self.request.query_params.get('periodo'):
            queryset = queryset.filter(period_academic__name=self.request.query_params.get('periodo'))
        if self.request.query_params.get('state'):
            queryset = queryset.filter(state=self.request.query_params.get('state'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProjectViewSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = ProjectViewSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = ProjectViewSerializer(obj, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class RUDProyectoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Project, id=self.kwargs['pk'])
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ProjectViewSerializer(obj, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListCreatePeriodAPIView(generics.ListCreateAPIView):
    serializer_class = PeriodAcademicSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = PeriodAcademic.objects.all().order_by('id')
        return queryset


class RUDPeriodAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PeriodAcademicSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(PeriodAcademic, id=self.kwargs['pk'])
        return obj
