# Generated by Django 5.1.5 on 2025-02-04 08:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
        ("routes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("user", "route")},
        ),
    ]
