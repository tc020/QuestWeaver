# Generated by Django 5.1.1 on 2024-09-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_ort_geographische_lage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ort',
            name='bedeutung_oder_funktion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='beschreibung_des_ortes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='bevölkerung_und_gesellschaft',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='flora_und_fauna',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='gefahren_und_bedrohungen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='gerüchte_und_legenden',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='historie_und_hintergrund',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='klima_und_wetter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='kulturelle_oder_religiöse_bedeutung',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='magische_oder_mystische_eigenschaften',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='politische_verhältnisse',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='quests_und_interaktionsmöglichkeiten',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='ressourcen_und_reichtümer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='verbindungen_zu_anderen_orten',
            field=models.TextField(blank=True, null=True),
        ),
    ]
