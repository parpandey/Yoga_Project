# Generated by Django 4.2.7 on 2023-11-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User_table",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("number", models.IntegerField(max_length=17)),
            ],
        ),
    ]
