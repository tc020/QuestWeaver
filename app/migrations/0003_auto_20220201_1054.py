# Generated by Django 3.2.5 on 2022-02-01 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220130_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reihenfolge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kapitelNr', models.IntegerField(blank=True, null=True)),
                ('chronologie', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='szene',
            name='kapitel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reihenfolge'),
        ),
    ]
