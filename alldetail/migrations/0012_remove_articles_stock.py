# Generated by Django 4.0.6 on 2022-09-05 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alldetail', '0011_allclientdata_wait_money_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='stock',
        ),
    ]
