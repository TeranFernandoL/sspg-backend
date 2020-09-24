from django.urls import path
from apps.faculties.views import *

app_name = "faculties"
urlpatterns = [
    path("schools", view=ListCreateSchoolAPIView.as_view(), name="LISTAR Y CREAR ESCUELA"),
    path("schools/<int:pk>", view=RUDSchoolAPIView.as_view(), name="RUD ESCUELA"),
    path("teacher", view=ListCreateTeacherAPIView.as_view(), name="LISTAR Y CREAR PROFESOR"),
    path("teacher/<int:pk>", view=RUDTeacherAPIView.as_view(), name="RUD PROFESOR"),
    path("student", view=ListCreateStudentAPIView.as_view(), name="LISTAR Y CREAR ESTUDIANTE"),
    path("student/available", view=ListStudentAvailableAPIView.as_view(), name="LISTAR ESTUDIANTES DISPONIBLES"),
    path("teacher/available", view=ListTeacherAvailableAPIView.as_view(), name="LISTAR PROFESORES DISPONIBLES"),
    path("student/<int:pk>", view=RUDStudentAPIView.as_view(), name="RUD ESTUDIANTE"),
]
