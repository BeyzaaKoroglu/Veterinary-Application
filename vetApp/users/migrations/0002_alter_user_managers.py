# Generated by Django 4.0.2 on 2022-02-08 23:05

from django.db import migrations

import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.managers.UserManager()),
            ],
        ),
    ]
