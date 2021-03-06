# Generated by Django 3.2.7 on 2021-09-25 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20210925_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='branch_course',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contact_course',
        ),
        migrations.AddField(
            model_name='category',
            name='category_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='myapi.course'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='branches',
        ),
        migrations.AddField(
            model_name='course',
            name='branches',
            field=models.ManyToManyField(to='myapi.Branch'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='contacts',
        ),
        migrations.AddField(
            model_name='course',
            name='contacts',
            field=models.ManyToManyField(to='myapi.Contact'),
        ),
    ]
