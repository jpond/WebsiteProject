from django.contrib import admin
from django.urls import path

from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('projects/', Projects.as_view()),
    path('resume/', Resume.as_view()),
]
