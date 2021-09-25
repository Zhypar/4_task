from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    imgpath = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'branches'
        verbose_name = 'branch'
    

    def __str__(self):
        return self.address

class Contact(models.Model):
    CONTACT_CHOICES = [
        ('1','PHONE'),
        ('2','FACEBOOK'),
        ('3','EMAIL'),
    ]
    type = models.CharField(max_length=30, choices = CONTACT_CHOICES)
    value = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'contacts'
        verbose_name = 'contact'
    

    def __str__(self):
        return self.value

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    logo = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contact)
    branches = models.ManyToManyField(Branch)
   
    class Meta:
        verbose_name_plural = 'courses'
        verbose_name = 'course'

    def __str__(self):
        return self.name