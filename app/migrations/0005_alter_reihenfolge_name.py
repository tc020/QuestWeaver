# Generated by Django 3.2.5 on 2022-02-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_reihenfolge_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reihenfolge',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
