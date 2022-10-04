from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from school.views import students_list


urlpatterns = [
    path('', students_list, name='student'),
    path('admin/', admin.site.urls),
]
