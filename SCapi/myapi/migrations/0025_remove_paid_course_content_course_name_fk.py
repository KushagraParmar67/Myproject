# Generated by Django 4.1.13 on 2024-03-26 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0024_coursecontent_course_pname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paid_course_content',
            name='Course_Name_FK',
        ),
    ]
