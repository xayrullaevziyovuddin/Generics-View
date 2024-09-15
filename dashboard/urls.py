from django.urls import path
from .views import (
    FacultyListView, FacultyDetailView, GroupListView, GroupDetailView,
    KafedraListView, KafedraDetailView, SubjectListView, SubjectDetailView,
    TeacherListView, TeacherDetailView, StudentListView, StudentDetailView
)

urlpatterns = [
    path('faculties/', FacultyListView.as_view(), name='faculty-list'),
    path('faculties/<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),

    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),

    path('kafedras/', KafedraListView.as_view(), name='kafedra-list'),
    path('kafedras/<int:pk>/', KafedraDetailView.as_view(), name='kafedra-detail'),

    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),

    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
