import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

# фикстуры
@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


# @pytest.fixture
# def settings():
#     return [:settings.MAX_STUDENTS_PER_COURSE]


# тесты
@pytest.mark.django_db
def test_get_one_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    response = client.get('api/v1/courses/?id=1')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == course['id']
    assert data[0]['name'] == course['name']


@pytest.mark.django_db
def test_get_course_list(client, courses_factory):
    courses = courses_factory(_quantity=15)
    response = client.get('api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_by_id(client, courses_factory):
    courses = courses_factory(_quantity=7)
    response = client.get(f'/api/v1/courses/?id={courses[2].id}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == courses[2].id


@pytest.mark.django_db
def test_filter_by_name(client, courses_factory):
    courses = courses_factory(_quantity=7)
    response = client.get(f'/api/v1/courses/?name={courses[2].name}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[2].name


@pytest.mark.django_db
def test_create_course(client, courses_factory, students_factory):
    count = Course.objects.count
    response = client.post('/api/v1/courses/', data={'name': 'Django', 'students': 'students.id'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, courses_factory, students_factory):
    courses = courses_factory(_quantity=12)
    new_course_name = 'Docker'
    response = client.patch('/api/v1/courses/{course[2].id}', data={'name': 'new_course_name', 'students': 'students.id'})
    new_course = client.get('/api/v1/courses/{course[2].id}').json()
    assert response.status_code == 201
    assert new_course['name'] == new_course_name


@pytest.mark.django_db
def test_delete_course(client, courses_factory, students_factory):
    courses = courses_factory(_quantity=12)
    response = client.get(f'/courses/')
    count = Course.objects.count()
    response = client.delete(f'/courses/{courses[2].id}/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1


# @pytest.mark.parametrize
# def test_validate_students(client, students_factory, settings):
#     pass