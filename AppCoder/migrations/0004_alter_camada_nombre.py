# Generated by Django 5.1.4 on 2024-12-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_camada_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camada',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]