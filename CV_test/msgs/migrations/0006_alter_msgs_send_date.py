# Generated by Django 5.0.4 on 2024-04-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0005_alter_msgs_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgs',
            name='send_date',
            field=models.CharField(max_length=100, verbose_name='Дата отправки'),
        ),
    ]
