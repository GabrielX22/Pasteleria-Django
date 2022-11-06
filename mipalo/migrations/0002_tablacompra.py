# Generated by Django 4.1.2 on 2022-11-06 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipalo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablacompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=15)),
                ('nombrecompra', models.CharField(max_length=100)),
                ('preciocompra', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cantidadcompra', models.IntegerField()),
                ('preciototal', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]