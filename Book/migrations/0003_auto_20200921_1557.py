# Generated by Django 3.1.1 on 2020-09-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_auto_20200915_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titele',
            new_name='title',
        ),
    ]
