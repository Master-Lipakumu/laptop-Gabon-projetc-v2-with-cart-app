# Generated by Django 4.0.6 on 2022-09-04 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docuclient', '0004_remove_facture_date_updated'),
        ('carts', '0002_transaction_remove_feature_articles_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_facturation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_facturation', to='docuclient.facture'),
        ),
    ]
