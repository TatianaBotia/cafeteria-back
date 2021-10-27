# Generated by Django 3.2.8 on 2021-10-15 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(default='')),
                ('apellido', models.IntegerField(default=0)),
                ('telefono', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='nombre',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='unitPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('totalPrice', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('dateOrder', models.DateTimeField(auto_now=True)),
                ('idClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.clients')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.product')),
            ],
        ),
    ]
