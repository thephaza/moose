# Generated by Django 5.1.3 on 2024-11-16 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
