# Generated by Django 4.2.6 on 2023-10-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_country_state_country_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='cod_tom',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
