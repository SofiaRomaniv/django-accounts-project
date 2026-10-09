from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return f"{self.profile} - {self.subject}"


class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return str(self.profile)


class Schedule(models.Model):
    datetime = models.DateTimeField()
    location = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.group} - {self.datetime}"
