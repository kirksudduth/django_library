# Generated by Django 3.0.9 on 2020-08-04 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_auto_20200804_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn_number',
            new_name='isbn',
        ),
    ]
