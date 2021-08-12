from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',views.UserView)
router.register('students',views.StudentView)
router.register('teachers',views.TeachertView)
router.register('subjects',views.SubjectView)
router.register('classrooms',views.ClassroomView)
router.register('grades',views.GradeView)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_school')),
    # Paths for Generics
    # path('generics/students/', views.StudentList.as_view()),
    # path('generics/students/<int:pk>', views.StudentDetail.as_view()),
    # path('generics/teachers/', views.TeachertList.as_view()),
    # path('generics/teachers/<int:pk>', views.TeachertDetail.as_view()),
    # path('generics/subjects/', views.SubjectList.as_view()),
    # path('generics/subjects/<int:pk>', views.SubjectDetail.as_view()),
    # path('generics/classrooms/', views.ClassroomList.as_view()),
    # path('generics/classrooms/<int:pk>', views.ClassroomDetail.as_view()),
    # path('generics/grades/', views.GradeList.as_view()),
    # path('generics/grades/<int:pk>', views.GradeDetail.as_view()),
]