# Generated by Django 4.0.4 on 2022-05-18 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Horreur', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='films',
            old_name='parution',
            new_name='date_de_sortie',
        ),
    ]
