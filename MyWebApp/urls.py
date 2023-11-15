from django.urls import path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('employees/', views.employeeList.as_view()),
]