# Generated by Django 5.1.1 on 2024-09-19 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_alter_szene_ort'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schauplatz_Ebene2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('schauplatz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.schauplatz')),
            ],
        ),
    ]
