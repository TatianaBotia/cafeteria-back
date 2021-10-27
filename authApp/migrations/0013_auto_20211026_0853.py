# Generated by Django 3.2.8 on 2021-10-26 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0012_alter_listproduct_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listproduct',
            name='idOrden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='authApp.order'),
        ),
        migrations.AlterField(
            model_name='listproduct',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='authApp.order'),
        ),
        migrations.AlterField(
            model_name='listproduct',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='authApp.order'),
        ),
    ]
