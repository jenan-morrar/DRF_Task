from django.contrib import admin
from .models import Student,Teacher,ClassRoom,Subject,Grade

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Grade)