# Generated by Django 4.1.13 on 2024-03-26 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0029_remove_paid_course_content_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_course_content',
            name='Course_FKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.particularcourse'),
        ),
    ]
