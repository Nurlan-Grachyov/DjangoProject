# Generated by Django 5.1.4 on 2025-01-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="year",
            field=models.CharField(
                choices=[
                    ("first", "Первый курс"),
                    ("second", "Второй курс"),
                    ("third", "Третий курс"),
                    ("fourth", "Четвертый курс"),
                ],
                default="first",
                max_length=6,
                verbose_name="Курс",
            ),
        ),
    ]
