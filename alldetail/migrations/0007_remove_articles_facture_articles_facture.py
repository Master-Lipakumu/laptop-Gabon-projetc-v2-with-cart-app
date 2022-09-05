# Generated by Django 4.0.6 on 2022-09-02 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docuclient', '0004_remove_facture_date_updated'),
        ('alldetail', '0006_articles_content_type_articles_object_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='facture',
        ),
        migrations.AddField(
            model_name='articles',
            name='facture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facture_article', to='docuclient.facture'),
        ),
    ]
