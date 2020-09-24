from django.urls import path
from apps.projects.views import *

app_name = "projects"
urlpatterns = [
    path("periodacademic", view=ListCreatePeriodAPIView.as_view(), name="PERIODO ACADEMICO"),
    path("periodacademic/<int:pk>", view=RUDPeriodAPIView.as_view(), name="RUD PERIODO"),
    path("", view=ListCreateProyectoAPIView.as_view(), name="LISTAR Y CREAR PROYECTO"),
    path("<int:pk>", view=RUDProyectoAPIView.as_view(), name="RUD PROYECTO"),
]
