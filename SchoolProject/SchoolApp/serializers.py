from rest_framework import serializers
from .models import Student,Subject,Grade,ClassRoom,Teacher

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['pk','gradeName']

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['pk','classRoomName']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['pk','subjectName','SubjectRoom','classRoomName']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentName','birthdate','studentSubjects','studentGrade']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacherName','teacherSubjects']
