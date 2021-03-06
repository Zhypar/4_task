# Generated by Django 3.2.7 on 2021-09-24 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210925_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_course', to='myapi.course'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_course', to='myapi.course'),
        ),
    ]
