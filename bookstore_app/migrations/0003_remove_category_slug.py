# Generated by Django 5.0.4 on 2024-05-17 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
