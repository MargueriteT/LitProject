# Generated by Django 3.2.7 on 2021-09-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='response',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
