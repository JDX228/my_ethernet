# Generated by Django 4.0.3 on 2022-03-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="new",
            name="news",
            field=models.TextField(max_length=200, unique=True, verbose_name="Новость"),
        ),
    ]
