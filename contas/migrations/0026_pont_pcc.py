# Generated by Django 2.2.1 on 2019-06-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0025_pont'),
    ]

    operations = [
        migrations.AddField(
            model_name='pont',
            name='pCC',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
