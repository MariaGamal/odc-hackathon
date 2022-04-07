from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course, name='course'),
    path('enroll/<int:course_id>', views.enroll, name='enroll'),
    path('code/<int:course_id>/', views.code, name='code'),
]
