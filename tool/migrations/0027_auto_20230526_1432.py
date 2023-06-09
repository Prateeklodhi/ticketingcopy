# Generated by Django 3.2.10 on 2023-05-26 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0026_auto_20230525_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AddField(
            model_name='ticket',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tool.category'),
        ),
    ]
