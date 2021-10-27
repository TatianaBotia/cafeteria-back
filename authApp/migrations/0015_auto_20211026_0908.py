# Generated by Django 3.2.8 on 2021-10-26 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0014_auto_20211026_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listproduct',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='authApp.product'),
        ),
        migrations.AlterField(
            model_name='listproduct',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
