
from django.db import models

class ClassRoom (models.Model):
    classRoomName = models.CharField(max_length=30,null=True)
    owner = models.ForeignKey('auth.user',related_name='ClassRooms', on_delete=models.CASCADE)
    def __str__(self):
        return self.classRoomName

class Subject (models.Model):
    subjectName = models.CharField(max_length=30,null=True)
    classRoomName = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, null=True, related_name='SubjectRoom')
    owner = models.ForeignKey('auth.user',related_name='Subjects', on_delete=models.CASCADE)
    def __str__(self):
        return self.subjectName

class Grade (models.Model):
    gradeName = models.CharField(max_length=30,null=True)
    owner = models.ForeignKey('auth.user',related_name='Grades', on_delete=models.CASCADE)
    def __str__(self):
        return self.gradeName


class Student (models.Model):
    studentName = models.CharField(max_length=30,null=True)
    birthdate = models.DateField(null=True)
    studentSubjects = models.ManyToManyField(Subject, related_name='studentSubjects')
    studentGrade = models.ForeignKey(Grade, on_delete=models.CASCADE,null=True,related_name='studentGrade')
    owner = models.ForeignKey('auth.user',related_name='Students', on_delete=models.CASCADE)
    def __str__(self):
        return self.studentName

class Teacher (models.Model):
    teacherName = models.CharField(max_length=30,null=True)
    teacherSubjects = models.ManyToManyField(Subject, related_name='teacherSubjects')
    owner = models.ForeignKey('auth.user',related_name='Teachers', on_delete=models.CASCADE)
    def __str__(self):
        return self.teacherName