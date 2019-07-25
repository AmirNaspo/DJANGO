# Generated by Django 2.2.1 on 2019-05-18 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_auto_20190517_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='empregado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('Observacoes', models.TextField(blank=True, null=True)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='puta',
        ),
    ]
