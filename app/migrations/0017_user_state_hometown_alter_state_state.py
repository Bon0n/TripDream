# Generated by Django 4.2.6 on 2023-10-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_user_interested_cities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state_hometown',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.CharField(max_length=40),
        ),
    ]
