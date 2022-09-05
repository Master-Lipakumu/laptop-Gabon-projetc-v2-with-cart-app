# Generated by Django 4.0.6 on 2022-09-02 07:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docuclient', '0004_remove_facture_date_updated'),
        ('alldetail', '0003_alter_articles_author_alter_articles_facture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='facture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facture_article', to='docuclient.facture'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='price',
            field=models.FloatField(default=25.0, null=True, validators=[django.core.validators.MinValueValidator(25.0)]),
        ),
        migrations.AlterField(
            model_name='articles',
            name='quantite_client',
            field=models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='articles',
            name='stock',
            field=models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
