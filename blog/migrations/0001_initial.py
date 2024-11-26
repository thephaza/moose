# Generated by Django 5.1.3 on 2024-11-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='posts/')),
                ('text', models.TextField()),
                ('author_name', models.CharField(max_length=25)),
                ('author_position', models.CharField(max_length=25)),
                ('author_image', models.ImageField(upload_to='posts/')),
                ('cretead_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
