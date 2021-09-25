
from django.urls import path

from .views import CategoryList, BranchList, ContactList, CourseList


app_name = "myapi"

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('branches/', BranchList.as_view()),
    path('contacts/', ContactList.as_view()),
    path('courses/', CourseList.as_view()),
]