from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:exam_id>/', views.exam, name='exam'),
]
