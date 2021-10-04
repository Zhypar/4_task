
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList, BranchList, ContactList, CourseList, CourseDetail


app_name = "myapi"

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('branches/', BranchList.as_view()),
    path('contacts/', ContactList.as_view()),
    path('courses/', CourseList.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view(),)
]