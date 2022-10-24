from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from students.filters import CourseFilter
from students.models import Course, Student
from students.serializers import CourseSerializer


class CoursesViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter


# class StudentsViewSet(ModelViewSet):
#
#     def validate_students(self, value):
#         students = Student.objects.count
#         if students > [:settings.MAX_STUDENTS_PER_COURSE]
#             raise ValidationError ('Превышено допустимое число студентов на курсе')
