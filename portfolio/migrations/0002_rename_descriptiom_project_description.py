# Generated by Django 4.0.4 on 2022-04-20 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
