from .models import Category, Branch, Contact, Course
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']

        def create(self, validated_data, *args, **kwargs):
            category = Category.objects.create(**validated_data)
            category.save()
            return category
    
        def __str__(self):
            return self.name


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']

    def create(self, validated_data, *args, **kwargs):
        branch = Contact.objects.create(*validated_data)
        branch.save()
        return Branch.objects.create(**validated_data)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

    def create(self, validated_data, *args, **kwargs):
        contact = Contact.objects.create(*validated_data)
        contact.save()
        return contact

class NestedBranchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Branch
        fields = '__all__'

class NestedContactSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    contacts = NestedContactSerializer(many = True)
    branches = NestedBranchSerializer(many = True)
    category = serializers.StringRelatedField()
    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')

        course = Course.objects.create(**validated_data)
        contacts = []
        branches = []
        for contact_data in contacts_data:
            contact_id = contact_data.pop('id', None)
            contact, _ = Contact.objects.get_or_create(id=contact_id,
                                                         defaults=contact_data)
            contacts.append(contact)

        for branch_data in branches_data:
            branch_id = branch_data.pop('id', None)
            branch, _ = Branch.objects.get_or_create(id=branch_id,
                                                        defaults=branch_data)
            branches.append(branch)

        course.contacts.add(*contacts)
        course.branches.add(*branches)

        return course
