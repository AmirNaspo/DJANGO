# Generated by Django 2.2.1 on 2019-05-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0009_empregado_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
