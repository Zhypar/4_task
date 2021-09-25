from django.shortcuts import render
from myapi.models import Category, Branch, Contact, Course
from myapi.serializers import CategorySerializer, BranchSerializer, ContactSerializer, CourseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryList(APIView):
    serializer_class = CategorySerializer

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

class BranchList(APIView):
    serializer_class = BranchSerializer

    def get(self, request, format=None):
        Branches = Branch.objects.all()
        serializer = BranchSerializer(Branches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.data.get('address')
            success = "Branch '{0}' has been added successfully".format(address)
            return Response({'success': success})
        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactList(APIView):

    serializer_class = ContactSerializer
    def get(self, request, format=None):
        Contacts = Contact.objects.all()
        serializer = ContactSerializer(Contacts, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            type = serializer.data.get('type')
            success = "Contact '{0}' has been added successfully".format(type)
            return Response({'success': success})

        else:
            return  Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class CourseList(APIView):

    serializer_class = CourseSerializer

    def get_queryset(self):
        courses = Course.objects.all()
        return courses

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                course = Course.objects.get(id=id)
                serializer = CourseSerializer(course)
        except:
            courses = self.get_queryset()
            serializer = CourseSerializer(courses, many = True)

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

    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                course = Course.objects.get(id=id)
                course.delete()
        except Course.DoesNotExist:
            return Response({'message': 'The course does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Course has been deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)