# Generated by Django 4.2.6 on 2023-10-24 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_city_uf_remove_state_ibge_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='country',
            new_name='country_id',
        ),
    ]
