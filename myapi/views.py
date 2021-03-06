from django.shortcuts import render,get_object_or_404
from myapi.models import Category, Branch, Contact, Course
from myapi.serializers import CategorySerializer, BranchSerializer, ContactSerializer, CourseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

class CategoryList(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, format=None):
        Categories = Category.objects.all()
        serializer = CategorySerializer(Categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchList(GenericAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    def get(self, request, format=None):
        Branches = Branch.objects.all()
        serializer = BranchSerializer(Branches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            address = serializer.data.get('address')
            success = "Branch '{0}' has been added successfully".format(address)
            return Response({'success': success})
        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactList(GenericAPIView):
    queryset = Contact.objects.all()

    serializer_class = ContactSerializer
    def get(self, request, format=None):
        Contacts = Contact.objects.all()
        serializer = ContactSerializer(Contacts, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            type = serializer.data.get('type')
            success = "Contact '{0}' has been added successfully".format(type)
            return Response({'success': success})

        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class CourseList(GenericAPIView):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request, format=None):
        Courses = Course.objects.all()
        serializer = CourseSerializer(Courses, many=True)
        return Response(serializer.data)  

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            success = "Course has been added successfully!"
            return Response({'success': success})
        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(GenericAPIView):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request, pk, format=None):
        course = get_object_or_404(Course, id=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)     

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)