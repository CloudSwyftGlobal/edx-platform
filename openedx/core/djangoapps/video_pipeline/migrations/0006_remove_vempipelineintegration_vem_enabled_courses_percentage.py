# Generated by Django 2.2.14 on 2020-08-07 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_pipeline', '0005_add_vem_course_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vempipelineintegration',
            name='vem_enabled_courses_percentage',
        ),
    ]
