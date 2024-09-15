from rest_framework import generics
from .models import Faculty, Group, Kafedra, Subject, Teacher, Student
from .serializers import (
    FacultySerializer, GroupSerializer, KafedraSerializer,
    SubjectSerializer, TeacherSerializer, StudentSerializer
)


# Faculty Views
class FacultyListView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class KafedraListView(generics.ListCreateAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class KafedraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class SubjectListView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
