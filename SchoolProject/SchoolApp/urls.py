from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students',views.StudentView)
router.register('teachers',views.TeachertView)
router.register('subjects',views.SubjectView)
router.register('classrooms',views.ClassroomView)
router.register('grades',views.GradeView)

urlpatterns = [
    path('',include(router.urls))
]