# Generated by Django 3.2.7 on 2021-09-25 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0013_auto_20210925_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_course', to='myapi.course'),
        ),
    ]
