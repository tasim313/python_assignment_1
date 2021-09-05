from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    st_id = models.CharField(max_length=264, verbose_name='ID', null=True, blank=True)
    name = models.CharField(max_length=264, verbose_name="Name", null=True, blank=True)
    age = models.CharField(max_length=264, verbose_name='Age', null=True, blank=True)
    Sex = models.CharField(max_length=30, verbose_name='Sex', null=True, blank=True)
    fatherName = models.CharField(max_length=264, verbose_name='Father Name', null=True, blank=True)
    motherName = models.CharField(max_length=264, verbose_name='Mother Name', null=True, blank=True)
    lastEducation = models.CharField(max_length=300, verbose_name='Last Education', null=True,  blank=True)