# Generated by Django 5.0 on 2024-01-13 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee", old_name="contact_number", new_name="contact",
        ),
    ]
