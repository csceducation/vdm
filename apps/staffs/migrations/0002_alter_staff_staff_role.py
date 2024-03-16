# Generated by Django 5.0.3 on 2024-03-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staffs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staff",
            name="staff_role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Administrative staff", "Administrative staff"),
                    ("Acadamic Staff", "Acadamic Staff"),
                    ("Acadamic & Administrator", "Acadamic & Administrator"),
                    ("other", "Other"),
                ],
                max_length=1024,
                verbose_name="Staff Role",
            ),
        ),
    ]