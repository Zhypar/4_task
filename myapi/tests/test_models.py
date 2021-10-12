from django.test import TestCase
from myapi.models import *

class TestCourse(TestCase):
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

    def test_course_name(self):
        result = Course.objects.get(id=1)
        expected_object = f'{result.name}'
        self.assertEqual(str(result), expected_object)

    def test_contact_value(self):
        result = Contact.objects.get(id=1)
        expected_object = f'{result.value}'
        self.assertEqual(str(result), expected_object)
        
    def test_branch_address(self):
        result = Branch.objects.get(id=1)
        expected_object = f'{result.address}'
        self.assertEqual(str(result), expected_object)
    
    def test_category_name(self):
        result = Category.objects.get(id=1)
        expected_object = f'{result.name}'
        self.assertEqual(str(result), expected_object)
        
