# Generated by Django 5.0.1 on 2024-01-09 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_course_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='link',
            new_name='teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='coupon',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lessons.course')),
            ],
        ),
    ]
