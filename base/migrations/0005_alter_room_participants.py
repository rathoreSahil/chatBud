# Generated by Django 4.1 on 2022-08-28 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_alter_room_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]