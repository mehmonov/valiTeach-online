# Generated by Django 5.0.1 on 2024-01-09 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_tokens_start_date'),
        ('lessons', '0004_lesson_name_alter_course_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='lessons.course'),
        ),
    ]
