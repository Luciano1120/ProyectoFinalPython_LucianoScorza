# Generated by Django 5.0 on 2024-01-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0002_cliente_cuit_alter_proveedor_condicion'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='CUIT',
            field=models.CharField(default='000', max_length=10),
        ),
    ]
