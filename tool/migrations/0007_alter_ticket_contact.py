# Generated by Django 3.2.10 on 2023-01-05 12:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0006_auto_20230105_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=12, region='IN'),
        ),
    ]