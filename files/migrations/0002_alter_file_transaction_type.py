# Generated by Django 4.1.5 on 2023-01-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='transaction_type',
            field=models.CharField(max_length=30),
        ),
    ]
