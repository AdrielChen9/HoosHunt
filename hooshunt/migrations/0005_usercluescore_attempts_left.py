# Generated by Django 4.2.4 on 2023-11-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hooshunt", "0004_merge_20231112_1215"),
    ]

    operations = [
        migrations.AddField(
            model_name="usercluescore",
            name="attempts_left",
            field=models.IntegerField(default=5),
        ),
    ]
