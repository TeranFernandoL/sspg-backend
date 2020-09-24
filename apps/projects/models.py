# Create your models here.
from django.db import models
from apps.behaviors import TimesStampedModel
from django.conf import settings
from enum import Enum
from jsonfield import JSONField
from apps.faculties.models import *


# Create your models here.
class PeriodAcademic(TimesStampedModel):
    name = models.CharField("Nombre", blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Periodo Academico"
        verbose_name_plural = "Periodos Academicos"


class Project(TimesStampedModel):
    class TypeState(Enum):
        PENDIENTE = "PENDIENTE"
        ACEPTADO = "ACEPTADO"
        SUSPENDIDO = "SUSPENDIDO"
        OBSERVADO = "OBSERVADO"
        ENTREGADO = "ENTREGADO"
        SUSTENTADO = "SUSTENTADO"

    class Type(Enum):
        TI = "TI"
        TESIS = "TESIS"
        TSP = "TSP"

    class InitialCourse(Enum):
        TESIS_1 = "TESIS_1"
        TESIS_2 = "TESIS_2"

    class GradeCourse(Enum):
        PREGRADO = "PREGRADO"
        POSGRADO = "POSGRADO"

    code = models.CharField("Codigo", blank=True, null=True, max_length=30)
    state = models.CharField("Estado", blank=True, null=True, max_length=40,
                             choices=[(item.name, item.value) for item in TypeState])
    type = models.CharField("Tipo", blank=True, null=True, max_length=20,
                            choices=[(item.name, item.value) for item in Type])
    student_1 = models.ForeignKey(Student, blank=True, null=True, related_name="projects_student1",
                                  on_delete=models.SET_NULL)
    student_2 = models.ForeignKey(Student, blank=True, null=True, related_name="projects_student2",
                                  on_delete=models.SET_NULL)
    student_3 = models.ForeignKey(Student, blank=True, null=True, related_name="projects_student3",
                                  on_delete=models.SET_NULL)
    adviser = models.ForeignKey(Teacher, blank=True, null=True, related_name="projects_adviser",
                                on_delete=models.SET_NULL)
    jury_1 = models.ForeignKey(Teacher, blank=True, null=True, related_name="projects_jury1",
                               on_delete=models.SET_NULL)
    jury_2 = models.ForeignKey(Teacher, blank=True, null=True, related_name="projects_jury2",
                               on_delete=models.SET_NULL)
    jury_3 = models.ForeignKey(Teacher, blank=True, null=True, related_name="projects_jury3",
                               on_delete=models.SET_NULL)
    num_doc_support = models.CharField("Numero de Resolucion Decanal", blank=True, null=True, max_length=100)
    date_doc_support = models.DateField("Fecha de Resolucion Decanal", blank=True, null=True)
    course_initial = models.CharField("Curso de Inicio", blank=True, null=True, max_length=40,
                                      choices=[(item.name, item.value) for item in InitialCourse])
    date_register = models.DateTimeField("Fecha de registro", blank=True, null=True)
    date_doc = models.DateTimeField("Fecha de Documento", blank=True, null=True)
    date_validity = models.DateTimeField("Fecha de Vigencia", blank=True, null=True)
    date_supporting = models.DateTimeField("Fecha de Sustentacion", blank=True, null=True)
    date_acceptance = models.DateTimeField("Fecha de Aceptacion", blank=True, null=True)
    congress = models.CharField("Congreso o Revista", blank=True, null=True, max_length=200)
    school = models.ForeignKey(School, blank=True, null=True, related_name="projects", on_delete=models.DO_NOTHING)
    name = models.CharField("Nombre", blank=True, null=True, max_length=200)
    grade = models.CharField("Grado", blank=True, null=True, max_length=50,
                             choices=[(item.name, item.value) for item in GradeCourse])
    period_academic = models.ForeignKey(PeriodAcademic,blank=True, null=True, related_name="proyects", on_delete=models.SET_NULL)


    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
