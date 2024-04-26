# Generated by Django 4.1.13 on 2024-03-03 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0016_alter_particularcourse_course_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='register',
            name='Purchased_Course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Purchased', to='myapi.particularcourse'),
            preserve_default=False,
        ),
    ]
