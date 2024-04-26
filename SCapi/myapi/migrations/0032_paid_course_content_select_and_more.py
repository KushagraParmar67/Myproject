# Generated by Django 4.1.13 on 2024-03-26 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0031_remove_paid_course_content_course_fkey_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paid_course_content',
            name='Select',
            field=models.CharField(choices=[('Java', 'Java'), ('Python', 'Python'), ('Dot_net', 'Dot_net'), ('Javascript', 'Javascript')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paid_course_content',
            name='Course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DEMOS', to='myapi.coursecontent'),
        ),
    ]