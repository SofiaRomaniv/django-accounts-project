from django.contrib import admin
from .models import Profile, Group, Teacher, Student, Schedule

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Schedule)