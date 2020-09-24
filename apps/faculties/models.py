from django.db import models
from apps.behaviors import TimesStampedModel
from django.conf import settings
from enum import Enum


class School(TimesStampedModel):
    code = models.CharField("Codigo de Escuela", blank=True, null=True, max_length=200)
    code_faculty = models.CharField("Codigo de Facultad", blank=True, null=True, max_length=200)
    name = models.CharField("Nombre de la Escuela", blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}-{}".format(self.id, self.name)

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"


class Student(TimesStampedModel):
    class TypeDocument(Enum):
        DNI = "DNI"
        PASSPORT = "PASSPORT"
        INMIGRATION_CARD = "INMIGRATION_CARD"

    class GradeCourse(Enum):
        PREGRADO = "PREGRADO"
        POSGRADO = "POSGRADO"

    code = models.CharField('Codigo', blank=True, null=True, max_length=20)
    type_document = models.CharField('Tipo de Documento', blank=True, null=True, max_length=30,
                                     choices=[(item.name, item.value) for item in TypeDocument])
    document = models.CharField('Nro Documento', blank=True, null=True, max_length=20)
    last_name = models.CharField("Apellidos", blank=True, null=True, max_length=40)
    first_name = models.CharField("Nombre", blank=True, null=True, max_length=40)
    email = models.EmailField("Email", blank=True, null=True, max_length=60)
    phone = models.CharField("Telefono", blank=True, null=True, max_length=20)
    address = models.CharField("Direccion", blank=True, null=True, max_length=20)
    photo = models.ImageField('Foto', upload_to='faculties/students', blank=True, null=True)
    semester_1 = models.BooleanField("Termino Semestre 1?", default=False)
    qualification_1 = models.FloatField("Calificacion Semestre 1", blank=True, null=True)
    semester_2 = models.BooleanField("Termino Semestre 2?", default=False)
    qualification_2 = models.FloatField("Calificacion Semestre 2", blank=True, null=True)
    grade = models.CharField("Grado", blank=True, null=True, max_length=50,
                             choices=[(item.name, item.value) for item in GradeCourse])

    def __str__(self):
        return "{} - {} {}".format(self.id, self.first_name, self.last_name)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


class Teacher(TimesStampedModel):
    class TypeDocument(Enum):
        DNI = "DNI"
        PASSPORT = "PASSPORT"
        INMIGRATION_CARD = "INMIGRATION_CARD"

    last_name = models.CharField("Apellidos", blank=True, null=True, max_length=40)
    first_name = models.CharField("Nombre", blank=True, null=True, max_length=40)
    email = models.EmailField("Email", blank=True, null=True, max_length=60)
    type_document = models.CharField('Tipo de Documento', blank=True, null=True, max_length=30,
                                     choices=[(item.name, item.value) for item in TypeDocument])
    document = models.CharField('Nro Documento', blank=True, null=True, max_length=20)
    asesor = models.BooleanField(default=False)
    phone = models.CharField(blank=True, null=True, max_length=10)
    codigo = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return "{} - {} {}".format(self.id, self.first_name, self.last_name)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
