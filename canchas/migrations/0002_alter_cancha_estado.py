# Generated by Django 5.1 on 2024-08-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("canchas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cancha",
            name="estado",
            field=models.CharField(
                choices=[("Disponible", "Disponible"), ("Ocupada", "Ocupada")],
                default="Disponible",
                max_length=20,
            ),
        ),
    ]