# Generated by Django 5.1.2 on 2024-10-12 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_periodic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='is_useful',
        ),
    ]
