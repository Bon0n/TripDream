# Generated by Django 4.2.6 on 2023-10-24 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_city_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.state'),
            preserve_default=False,
        ),
    ]