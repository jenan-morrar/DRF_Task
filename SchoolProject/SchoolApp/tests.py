import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from .models import Student, Subject, Teacher, ClassRoom, Grade


class StudentTestCase(APITestCase):
    list_url = reverse("student-list")

    def setUp(self):
        self.username = 'admin4'
        self.password = 'admin4'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)

    # Example of get
    def test_1(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeacherTestCase(APITestCase):
    def setUp(self):
        self.username = 'admin4'
        self.password = 'admin4'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        self.classroom = ClassRoom.objects.create(classRoomName="old room", owner=self.user)
        self.subject = Subject.objects.create(subjectName='math', classRoomName=self.classroom,owner=self.user)
        self.teacher = Teacher.objects.create(teacherName='mustafa', owner=self.user)
        self.teacher.teacherSubjects.add(self.subject)

    def test_1(self):
        # Example of retrieve
        response = self.client.get(reverse("teacher-detail", kwargs={"pk": self.teacher.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubjectTestCase(APITestCase):
    def setUp(self):
        self.username = 'admin4'
        self.password = 'admin4'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        self.classroom = ClassRoom.objects.create(classRoomName="old room", owner=self.user)
        self.subject = Subject.objects.create(subjectName='math', classRoomName=self.classroom,owner=self.user)

    def test_1(self):
        # Example of delete
        response = self.client.delete(reverse("subject-detail", kwargs={'pk': self.subject.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GradeTestCase(APITestCase):
    list_url = reverse("grade-list")

    def setUp(self):
        self.username = 'admin4'
        self.password = 'admin4'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)

    def test_1(self):
        # Example of Post
        response = self.client.post(self.list_url, {'gradeName': 'new grade'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ClassroomTestCase(APITestCase):
    def setUp(self):
        self.username = 'admin4'
        self.password = 'admin4'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
        self.classroom = ClassRoom.objects.create(classRoomName="old room", owner= self.user)

    def test_1(self):
        # Example of put (update)
        response = self.client.put(reverse("classroom-detail", kwargs={'pk': self.classroom.pk}), {"classRoomName": "new room"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
