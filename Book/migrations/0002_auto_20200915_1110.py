# Generated by Django 3.1.1 on 2020-09-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='titele',
            field=models.CharField(max_length=40),
        ),
    ]
