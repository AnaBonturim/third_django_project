# Generated by Django 5.0.4 on 2024-10-16 14:57

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
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='default.png', upload_to='images')),
                ('excerpt', models.CharField(blank=True, max_length=500)),
                ('content', models.TextField()),
            ],
        ),
    ]
