# Generated by Django 2.2.1 on 2019-05-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0008_auto_20190518_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='DJANGO/'),
        ),
    ]
