# Generated by Django 5.1.1 on 2024-09-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_ort_bedeutung_oder_funktion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ortliste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kommentar', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
