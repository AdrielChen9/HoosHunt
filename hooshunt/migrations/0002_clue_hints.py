# Generated by Django 4.2.5 on 2023-11-10 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooshunt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='hints',
            field=models.CharField(default='', max_length=700),
        ),
    ]
