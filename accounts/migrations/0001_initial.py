# Generated by Django 2.2.1 on 2019-05-29 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='empregado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('Observacoes', models.TextField(blank=True, null=True)),
                ('Foto', models.FileField(upload_to='images/')),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Categoria')),
            ],
        ),
    ]
