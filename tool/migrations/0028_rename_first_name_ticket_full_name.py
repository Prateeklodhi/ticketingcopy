# Generated by Django 3.2.10 on 2023-05-26 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0027_auto_20230526_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='first_name',
            new_name='full_name',
        ),
    ]