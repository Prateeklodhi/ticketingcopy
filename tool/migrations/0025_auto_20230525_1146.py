# Generated by Django 3.2.10 on 2023-05-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0024_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('Critical', 'Critical'), ('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low'), ('Very Low', 'Very Low')], default='Normal', max_length=60),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Reopened', 'Reopened'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Open', max_length=60),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type_of_problem',
            field=models.CharField(choices=[('MMU', 'MMU'), ('Website', 'Website'), ('Treatment', 'Treatment'), ('Other', 'Other')], default='Other', max_length=60),
        ),
    ]