# Generated by Django 3.2.13 on 2022-06-09 06:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20220607_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='creat_at',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='creat_at',
            new_name='create_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='image_likes',
            field=models.ManyToManyField(blank=True, related_name='post_image_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
