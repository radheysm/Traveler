# Generated by Django 2.1.7 on 2020-02-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roame', '0003_auto_20200221_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
