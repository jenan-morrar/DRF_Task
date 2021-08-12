from rest_framework import serializers
from .models import Student,Subject,Grade,ClassRoom,Teacher
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    Students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    Teachers = serializers.PrimaryKeyRelatedField(many=True, queryset=Teacher.objects.all())
    Subjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())
    ClassRooms = serializers.PrimaryKeyRelatedField(many=True, queryset=ClassRoom.objects.all())
    Grades = serializers.PrimaryKeyRelatedField(many=True, queryset=Grade.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['pk','username','Students','Teachers','Subjects','ClassRooms','Grades','owner']



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
        fields = ['pk','subjectName','classRoomName']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentName','birthdate','studentSubjects','studentGrade']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacherName','teacherSubjects']
