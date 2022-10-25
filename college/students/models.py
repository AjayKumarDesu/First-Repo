from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    objects = None
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_phone = models.IntegerField()
    ssc_marks = models.FileField(upload_to='media/')
    inter_marks = models.FileField(upload_to='media/')
    is_verified = models.BooleanField(default=False)

    def __str__(self):

        return self.student_name


class Department(models.Model):
    objects = None
    code = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)


class Register(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Student = models.OneToOneField(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='media/', null=True, blank=True)


class Staff(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=50)
    staff_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    staff_email = models.EmailField()
    staff_phone = models.IntegerField()
    qualification = models.TextField()
    experience = models.IntegerField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.staff_phone
