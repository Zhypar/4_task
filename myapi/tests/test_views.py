from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.urls import reverse
from django.test import TestCase
from myapi.models import *
from myapi.views import *




class TestCourse(APITestCase):
    url_courses = '/api/courses/'
    url_courses_detail = '/api/courses/?id=1/'
    url_contacts = '/api/contacts/?'
    url_branches = '/api/branches/?'
    url_categories = '/api/categories/?'

    def setUp(self):

        test_category = Category.objects.create(name='Sport', imgpath = "jpg")
        test_branch = Branch.objects.create(latitude = 12, longitude = 12, address = "Mira")
        test_contact = Contact.objects.create(type = "1", value = "9876543")

        test_course = Course.objects.create(
            name='Swimming',
            description='text',
            logo='jpg',
            category = test_category,
        )

        contact_objects_for_course = Contact.objects.all()
        test_course.contacts.set(contact_objects_for_course)
        test_course.save()

        branch_objects_for_course = Branch.objects.all()
        test_course.branches.set(branch_objects_for_course)
        test_course.save()    


    def test_get_courses(self):
        response = self.client.get(self.url_courses)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], "Swimming")

    def test_get_a_course(self):
        response = self.client.get(self.url_courses_detail)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['name'], "Swimming")

    def test_post_a_course(self):

        data = {
            "id": 8,
            "name": "Piano",
            "description": "text",
            "category": 1,
            "logo": "image",
            "contacts": [{
                "type": "1",
                "value": "89898989"}],
            "branches": [{
                "latitude": 1,
                "longitude": 2,
                "address": "Mira"}]
        }
        response = self.client.post(self.url_courses, data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, 200)



class TestsAPIListDetailView(TestCase):

    url_courses = '/api/courses/?'

    def setUp(self):
        self.factory = APIRequestFactory()        
        test_category = Category.objects.create(name='Sport', imgpath = "jpg")
        test_branch = Branch.objects.create(latitude = 12, longitude = 12, address = "Mira")
        test_contact = Contact.objects.create(type = "1", value = "9876543")

        self.test_course = Course.objects.create(
            name='Swimming',
            description='text',
            logo='jpg',
            category = test_category,
        )

        contact_objects_for_course = Contact.objects.all()
        self.test_course.contacts.set(contact_objects_for_course)
        self.test_course.save()

        branch_objects_for_course = Branch.objects.all()
        self.test_course.branches.set(branch_objects_for_course)
        self.test_course.save() 

    def test_delete_a_course(self):

   

        req = self.factory.delete("{}{}/?q=bar".format(self.url_courses, self.test_course.pk))
        resp = CourseDetail.as_view()(req, pk=self.test_course.pk)

        self.assertEqual(204, resp.status_code)