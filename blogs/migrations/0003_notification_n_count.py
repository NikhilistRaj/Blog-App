# Generated by Django 3.0.8 on 2021-06-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='n_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]