# Generated by Django 4.0.6 on 2022-09-05 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_order_cart_facturation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alldetail', '0009_allclientdata_remove_administrationclient_author_and_more'),
        ('users', '0004_remove_profile_administrationclients_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdministrationClient',
        ),
        migrations.DeleteModel(
            name='ClientParticulier',
        ),
        migrations.DeleteModel(
            name='ConventionEntrepriseClient',
        ),
        migrations.DeleteModel(
            name='EntrepriseClient',
        ),
        migrations.AddField(
            model_name='allclientdata',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='allclientdata',
            name='client_cart_facturation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_cart_facturation', to='carts.order'),
        ),
        migrations.AddField(
            model_name='allclientdata',
            name='client_cart_facturation_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_cart_facturation_2', to='carts.orderitem'),
        ),
    ]
