from django.db import models
from django.utils import timezone


class Kapitel(models.Model):
    name = models.CharField(max_length=200)
    kapitelNr = models.IntegerField(unique=True)
    kommentar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Szene(models.Model):
    name = models.CharField(max_length=200)
    kapitel = models.ForeignKey(to="Kapitel", on_delete=models.CASCADE)
    chronologie = models.IntegerField()
    ort = models.ForeignKey(to="Ortliste", on_delete=models.CASCADE)
    beschreibung = models.TextField(null=True, blank=True)
    kommentar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Figur(models.Model):
    name = models.CharField(max_length=200)
    geschlecht = models.CharField(max_length=200, null=True, blank=True)
    beruf = models.CharField(max_length=200, null=True, blank=True)
    rasse = models.CharField(max_length=200, default="Mensch", null=True, blank=True)
    figurenliste = models.ForeignKey(to="Figurenliste", on_delete=models.CASCADE, null=True, blank=True)
    alive = models.BooleanField(default=True)
    plot = models.CharField(max_length=200, default="None")
    kommentar = models.TextField(null=True, blank=True)
    ort = models.ForeignKey(to="Ort", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Figurenliste(models.Model):
    name = models.CharField(max_length=200)
    kommentar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Ortliste(models.Model):
    name = models.CharField(max_length=200)
    kommentar = models.TextField(null=True, blank=True)
    
    geographische_lage = models.CharField(max_length=200, null=True, blank=True)
    beschreibung_des_ortes = models.TextField(null=True, blank=True)
    bevölkerung_und_gesellschaft = models.TextField(null=True, blank=True)
    quests_und_interaktionsmöglichkeiten = models.TextField(null=True, blank=True)
    gefahren_und_bedrohungen = models.TextField(null=True, blank=True)
    gerüchte_und_legenden = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Ort(models.Model):
    name = models.CharField(max_length=200)
    alive = models.BooleanField(default=True)
    kommentar = models.TextField(null=True, blank=True)
    beschreibung = models.TextField(null=True, blank=True)

    ortliste = models.ForeignKey(to="Ortliste", on_delete=models.CASCADE, null=True, blank=True)

    #Felder für mehr Details
    typ = models.CharField(max_length=200, null=True, blank=True)  # z.B. Wirtshaus, Burg, Markt
    architektur = models.CharField(max_length=200, null=True, blank=True)  # z.B. gotisch, barock, rustikal
    zustand = models.CharField(max_length=200, null=True, blank=True)  # z.B. gut erhalten, baufällig
    besitzer = models.CharField(max_length=200, null=True, blank=True)  # Der aktuelle Besitzer oder Herrscher
    wichtige_personen = models.TextField(null=True, blank=True)  # Wichtige NPCs, die hier angetroffen werden können
    geschichte_des_schauplatzes = models.TextField(null=True, blank=True)  # Historie des Gebäudes oder Platzes
    bedeutung_oder_funktion = models.CharField(max_length=200, null=True, blank=True)  # z.B. Handelszentrum, Gasthaus
    quests_und_interaktionsmöglichkeiten = models.TextField(null=True, blank=True)  # Potenzielle Aufgaben oder NPC-Interaktionen
    gefahren_und_bedrohungen = models.TextField(null=True, blank=True)  # z.B. Räuberüberfälle, magische Gefahren
    geheimnisse_und_legenden = models.TextField(null=True, blank=True)  # Versteckte Informationen oder Mythen

    def __str__(self):
        return self.name 

class Schauplatz(models.Model):
    name = models.CharField(max_length=200)
    alive = models.BooleanField(default=True)
    kommentar = models.TextField(null=True, blank=True)
    ortliste = models.ForeignKey(to="Ort", on_delete=models.CASCADE, null=True, blank=True) #FK

    #Felder für mehr Details
    raumtyp = models.CharField(max_length=200, null=True, blank=True)  # z.B. Schankraum, Bibliothek, Kerker
    einrichtungsstil = models.CharField(max_length=200, null=True, blank=True)  # z.B. rustikal, prunkvoll, spärlich
    beleuchtung = models.CharField(max_length=200, null=True, blank=True)  # z.B. Fackeln, magische Lichter, Kerzen
    zustand = models.CharField(max_length=200, null=True, blank=True)  # z.B. sauber, verfallen, renoviert
    nutzung = models.CharField(max_length=200, null=True, blank=True)  # z.B. Wohnraum, Verlies, Lagerraum
    spezielle_gegenstände = models.TextField(null=True, blank=True)  # z.B. wertvolle Möbel, Artefakte
    gefahren_und_bedrohungen = models.TextField(null=True, blank=True)  # z.B. Fallen, Monster
    geheimnisse_und_versteckte_elemente = models.TextField(null=True, blank=True)  # Versteckte Türen, Fallen, Geheimfächer
    quests_und_interaktionsmöglichkeiten = models.TextField(null=True, blank=True)  # Interaktionen, die in diesem Raum stattfinden können

    def __str__(self):
        return self.name
