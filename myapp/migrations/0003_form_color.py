# Generated by Django 3.0.2 on 2020-03-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
    ]