# Generated by Django 5.0.4 on 2024-10-26 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_author_email_address_alter_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author'),
        ),
    ]
