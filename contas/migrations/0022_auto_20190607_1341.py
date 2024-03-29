# Generated by Django 2.2.1 on 2019-06-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0021_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numIng', models.CharField(max_length=120)),
                ('nomeIng', models.CharField(max_length=120)),
                ('umidade', models.CharField(max_length=120)),
                ('energiaKCal', models.CharField(max_length=120)),
                ('energiaKJ', models.CharField(max_length=120)),
                ('proteina', models.CharField(max_length=120)),
                ('lipideos', models.CharField(max_length=120)),
                ('colesterol', models.CharField(max_length=120)),
                ('carboidrato', models.CharField(max_length=120)),
                ('fibraAlimentar', models.CharField(max_length=120)),
                ('cinzas', models.CharField(max_length=120)),
                ('calcio', models.CharField(max_length=120)),
                ('magnesio', models.CharField(max_length=120)),
                ('manganes', models.CharField(max_length=120)),
                ('fosforo', models.CharField(max_length=120)),
                ('ferro', models.CharField(max_length=120)),
                ('sodio', models.CharField(max_length=120)),
                ('potassio', models.CharField(max_length=120)),
                ('cobre', models.CharField(max_length=120)),
                ('zinco', models.CharField(max_length=120)),
                ('retinol', models.CharField(max_length=120)),
                ('RE', models.CharField(max_length=120)),
                ('RAE', models.CharField(max_length=120)),
                ('tiamina', models.CharField(max_length=120)),
                ('riboflavina', models.CharField(max_length=120)),
                ('piridoxina', models.CharField(max_length=120)),
                ('niacina', models.CharField(max_length=120)),
                ('vitaminaC', models.CharField(max_length=120)),
                ('Q1', models.CharField(max_length=120)),
                ('DS1', models.CharField(max_length=120)),
                ('DZ1', models.CharField(max_length=120)),
                ('V1', models.CharField(max_length=120)),
                ('DZDNS', models.CharField(max_length=120)),
                ('DZTNT', models.CharField(max_length=120)),
                ('V4', models.CharField(max_length=120)),
                ('V5', models.CharField(max_length=120)),
                ('VD5', models.CharField(max_length=120)),
                ('VD6', models.CharField(max_length=120)),
                ('DZ1t', models.CharField(max_length=120)),
                ('DZ2t', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='id',
        ),
    ]
