# Generated by Django 4.1.2 on 2022-11-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipalo', '0006_tablacompra_compraimagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablacompra',
            name='fechacompras',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tablaproducto',
            name='fechaproducto',
            field=models.DateField(null=True),
        ),
    ]
