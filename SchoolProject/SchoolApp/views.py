from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Student,Teacher,Subject,ClassRoom,Grade
from .serializers import StudentSerializer,TeacherSerializer,SubjectSerializer,ClassRoomSerializer,GradeSerializer,UserSerializer

# *************** using ViewSets *********************

class UserView(viewsets.ModelViewSet):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TeachertView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClassroomView(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GradeView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# *************** using Generic *********************

"""class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeachertList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeachertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ClassroomList(generics.ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer


class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer"""
