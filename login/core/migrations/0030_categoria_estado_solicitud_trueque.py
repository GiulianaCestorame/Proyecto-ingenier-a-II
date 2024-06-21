# Generated by Django 5.0.4 on 2024-06-05 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_solicitud_realizado_alter_publicacion_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trueque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='core.trueque'),
        ),
    ]
