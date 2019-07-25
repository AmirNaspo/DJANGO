# Generated by Django 2.2.1 on 2019-06-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0022_auto_20190607_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutri',
            name='DS1',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='DZ1',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='DZ1t',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='DZ2t',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='DZDNS',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='DZTNT',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='Q1',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='RAE',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='RE',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='V1',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='V4',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='V5',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='VD5',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='VD6',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='calcio',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='carboidrato',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='cinzas',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='cobre',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='colesterol',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='energiaKCal',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='energiaKJ',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='ferro',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='fibraAlimentar',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='fosforo',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='lipideos',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='magnesio',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='manganes',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='niacina',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='piridoxina',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='potassio',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='proteina',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='retinol',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='riboflavina',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='sodio',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='tiamina',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='umidade',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='vitaminaC',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='nutri',
            name='zinco',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]