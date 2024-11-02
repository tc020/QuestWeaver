from django.shortcuts import render, redirect, get_object_or_404
from . import models
from app.tests import *
from django.http import HttpResponse
from .scripts.gpt_ort import ort_erzeugen, nsc_erzeugen

def home(request):
    szenen = models.Szene.objects.all()
    if request.POST: #prüft ob ein Request reinkommt
        var1 = request.POST["sortierung"]
        if var1 == "kapitel":
            szenen = models.Szene.objects.all().order_by("kapitel") #sortieren nach Kapitelnummern
        if var1 == "chronologie":
            szenen = models.Szene.objects.all().order_by("chronologie") #sortieren nach Chronologienummern
    figuren = models.Figur.objects.all()
    context = {"szenen": szenen, "figuren": figuren}
    return render(request, "home.html", context)

def navbar(request):
    return render(request, "navbar.html", context)

def header(request):
    return render(request, "header.html", context)

def figuren(request):
    figurenlisten = models.Figurenliste.objects.all()
    context = {"figurenlisten": figurenlisten}
    return render(request, "figuren.html", context)

def orte(request, ortlisten_id):
    schauplätze = []
    ortliste = get_object_or_404(models.Ortliste, pk=ortlisten_id)
    schauplatz = models.Ort.objects.filter(ortliste="8")
    figurenliste = get_object_or_404(models.Figurenliste, pk="17")
    for i in schauplatz:
        o = str(i)
        schauplätze.append(o)
    orte = models.Ort.objects.filter(ortliste=ortliste)
    auswahl = models.Ortliste.objects.all()
    """for f in schauplatz: #for-schleife funktioniert. War ein Test zum automatischen generieren und anlegen von NSCs pro Schauplatz. Sollte aber vllt in einem sepearaten View abgehandelt werden. Sollte nicht zu viel auf ein mal und gleichzeitig wollen und machen. 
        nsc = nsc_erzeugen(ortliste.geographische_lage, ortliste.beschreibung_des_ortes, ortliste.bevölkerung_und_gesellschaft, ortliste.gerüchte_und_legenden, 
                       ortliste.quests_und_interaktionsmöglichkeiten, ortliste.gefahren_und_bedrohungen, str(f))
        for o in nsc:
            print("NSC:",o)
        print("--------------------------------------------------------------------")
        #ortliste = get_object_or_404(models.Ortliste, pk=ort[0].id)
        models.Figur.objects.create(name="TÖST", plot="TEEEEEST", figurenliste=figurenliste, kommentar="NSC", ort=f)
        print("FIGUR TÖST WURDE ANGELEGT.")"""
    if request.POST:
        ortliste.kommentar = request.POST["orte_kommentar"]
        ortliste.save()
        return redirect("orte_edit", ortliste.id)    
    #ortliste = models.Ortliste.objects.all()
    context = {"ortliste": ortliste, "orte": orte, "auswahl": auswahl}
    return render(request, "orte.html", context)

def orte_edit(request, orte_id): #checken
    orteliste = get_object_or_404(models.Ortliste, pk=orte_id) # prüft ob model und darin enthaltenes objekt existieren. falls nicht = Fehler 404
    orte = models.Szene.objects.filter(ort=orteliste) #filtern nach ort in model Szene anhand des primary keys
    if request.POST:
        orteliste.kommentar = request.POST["orte_kommentar"]
        orteliste.save()
        return redirect("orte", orteliste.id)
    context = {"orte": orte, "orteliste": orteliste}
    return render(request, "orte_edit.html", context)

def kapitel(request):
    kapitel = models.Kapitel.objects.all()
    context = {"kapitel": kapitel}
    return render(request, "kapitel.html", context)

def kapitel_anlegen(request):
    models.Kapitel.objects.create(name=request.POST["kapitel_name"], kapitelNr=request.POST["kapitel_nummer"]) #request.POST überprüft vorher ob in dem Feld überhaupt was steht
    return redirect("kapitel")

def delete_kapitel(request, kapitel_id):
  kapitel = models.Kapitel.objects.get(id=kapitel_id)
  kapitel.delete()
  return redirect('kapitel')

def szenen(request, szene_id):
    kapitelliste = get_object_or_404(models.Kapitel, pk=szene_id)
    orte = models.Ortliste.objects.all()
    szenen = models.Szene.objects.filter(kapitel=kapitelliste)
    if request.POST:
        kapitelliste.kommentar = request.POST["kapitel_kommentar"]
        kapitelliste.save()
        return redirect("szenen", kapitelliste.id)
    context = {"szenen": szenen, "kapitelliste": kapitelliste, "orte": orte}
    return render(request, "szenen.html", context)

def szene_anlegen(request):
    if request.POST:
        szenenname = request.POST.get('szene_name')
        chronologie = request.POST.get('chronologie')
        #ort = request.POST.get('ort_name')
        ort = get_object_or_404(models.Ortliste, pk=request.POST["ort_name"])
        szene_id = request.POST.get('kapitelnr')
        kapitelnr = get_object_or_404(models.Kapitel, pk=request.POST["kapitelnr"])
    print(szenenname, chronologie, ort, kapitelnr)
    models.Szene.objects.create(name=szenenname, kapitel=kapitelnr, chronologie=chronologie, ort=ort) 
    return redirect("szenen", szene_id)

def szene_edit(request, szeneedit_id):
    szene_edit = get_object_or_404(models.Szene, pk=szeneedit_id)
    szenen = models.Szene.objects.all()
    if request.POST:
        szene_edit.name = request.POST["name"]
        #szene_edit.kapitel = request.POST["nummer"]
        szene_edit.chronologie = request.POST["chronologie"]
        szene_edit.ort = request.POST["ort"]
        szene_edit.beschreibung = request.POST["beschreibung"]
        szene_edit.kommentar = request.POST["szene_kommentar"]
        szene_edit.save()
        return redirect("szenen", szene_edit.kapitel.id)
    context = {"szenen": szenen, "szene_edit": szene_edit}
    return render(request, "szene_edit.html", context)

def delete_szene(request):
  if request.method == 'POST':
        parameter1 = request.POST.get('parameter1')
        szene_id = request.POST.get('parameter2')
  figurenliste = models.Szene.objects.get(id=parameter1)
  figurenliste.delete()
  return redirect('szenen', szene_id)

def listen(request, listen_id):
    figurenlisten = get_object_or_404(models.Figurenliste, pk=listen_id)
    figuren = models.Figur.objects.filter(figurenliste=figurenlisten)
    auswahl = models.Figurenliste.objects.all()
    if request.POST:
        figurenlisten.kommentar = request.POST["figurenliste_kommentar"]
        figurenlisten.save()
        return redirect("listen", figurenlisten.id)
    context = {"figurenlisten": figurenlisten, "figuren": figuren, "auswahl": auswahl}
    return render(request, "listen.html", context)

def figurenliste_anlegen(request):
    models.Figurenliste.objects.create(name=request.POST["figurenliste_name"]) #request.POST überprüft vorher ob in dem Feld überhaupt was steht
    return redirect("figuren")

def delete_figur(request, figur_id):
  figurtyp = models.Figurenliste.objects.get(id=figur_id)
  figurtyp.delete()
  return redirect('figuren')

def delete_figurenliste(request):
  if request.method == 'POST':
        parameter1 = request.POST.get('parameter1')
        figurenliste_id = request.POST.get('parameter2')
  figurenliste = models.Figur.objects.get(id=parameter1)
  figurenliste.delete()
  return redirect('listen', figurenliste_id)

def figur_anlegen(request):
    figurenliste = get_object_or_404(models.Figurenliste, pk=request.POST["figur_figurenliste"])
    try: 
        schauplatz_id = request.POST["ort_id"]
        ort = get_object_or_404(models.Ort, pk=request.POST["ort_id"])
        models.Figur.objects.create(name=request.POST["figur_name"], figurenliste=figurenliste, ort=ort)
        return redirect("schauplatz", schauplatz_id)
    except:
        models.Figur.objects.create(name=request.POST["figur_name"], figurenliste=figurenliste) #request.POST überprüft vorher ob in dem Feld überhaupt was steht
    listen_id = int(request.POST["figur_figurenliste"]) #String in Integer umwandeln, damit es sauber weiterverarbeitet werden kann
    return redirect("listen", listen_id)

def figuren_edit(request, figuren_id):
    figuren_edit = get_object_or_404(models.Figur, pk=figuren_id)
    figuren = models.Figur.objects.all()
    figurenlisten = models.Figurenliste.objects.all()
    orte = models.Ort.objects.all()
    if request.POST:
        figurenlistenid = int(request.POST["figur_figurenliste"])-1 #index-1 da ab 0 gezählt wird 
        figurenortid = int(request.POST["figur_ort"]) #index-1 da ab 0 gezählt wird 
        figuren_edit.name = request.POST["figur_name"]
        figuren_edit.geschlecht = request.POST["figur_geschlecht"]
        figuren_edit.beruf = request.POST["figur_beruf"]
        figuren_edit.rasse = request.POST["figur_rasse"]
        figuren_edit.alive = "figur_alive" in request.POST
        figuren_edit.figurenliste = figurenlisten[figurenlistenid]
        for i in orte:
            if i.id == figurenortid:
                figuren_edit.ort = i
        figuren_edit.kommentar = request.POST["figur_kommentar"]
        figuren_edit.save()
        return redirect("figuren_edit", figuren_edit.id)
    context = {"figuren_edit": figuren_edit, "figuren": figuren, "figurenlisten": figurenlisten, "orte": orte}
    return render(request, "figuren_edit.html", context)

# ----------------------------------------------------------------------------------------------------------> Unnötiger view? Wird nicht verwendet
def schauplatz_ebene2(request, ortlisten_id):
    schauplaetze = get_object_or_404(models.Schauplatz, pk=ortlisten_id)
    orte = models.Ort.objects.filter(ortliste=ortliste)
    auswahl = models.Ortliste.objects.all()
    
    #ortliste = models.Ortliste.objects.all()
    context = {"ortliste": ortliste, "orte": orte, "auswahl": auswahl}
    return render(request, "orte_ebene2.html", context)
#------------------------------------------------------------------------------------------------------------<

def ortliste(request):
    ortliste = models.Ortliste.objects.all()
    if request.method == 'POST':
        typ = request.POST["typ"]
        geo = request.POST["geo"]
        gross = request.POST["gross"]
        zustand = request.POST["zustand"]
        ort_info = ort_erzeugen(typ, geo, gross, zustand)
        #print("Es gibt:",ort_info.anzahl_der_wirtshäuser,"Wirtshäuser.")
        models.Ortliste.objects.create(name=ort_info.name, kommentar="Ort vom Co-Meister erzeugt", beschreibung_des_ortes=ort_info.beschreibung_des_ortes, bevölkerung_und_gesellschaft=ort_info.bevölkerung_und_gesellschaft, gerüchte_und_legenden=ort_info.gerüchte_und_legenden, quests_und_interaktionsmöglichkeiten=ort_info.quests_und_interaktionsmöglichkeiten, 
                                       gefahren_und_bedrohungen=ort_info.gefahren_und_bedrohungen, geographische_lage=ort_info.geographische_lage)
        #print("Besondere Orte:",ort_info["Besonderen Orte"])
        for specialort in ort_info.besonderen_orte:
            #print("Der besondere Ort lautet:",specialort["name"])
            #print("Orts-Typ:",specialort["ortstyp"])
            #print("Ortsbeschreibung:",specialort["beschreibung"])
            ort = models.Ortliste.objects.filter(name=ort_info.name)
            ortliste = get_object_or_404(models.Ortliste, pk=ort[0].id)
            models.Ort.objects.create(name=specialort["name"], typ=specialort["ortstyp"], ortliste=ortliste, beschreibung=specialort["beschreibung"])
            #print("Schauplatz erfolgreich angelegt.")
        
        for wirtshaus in ort_info.wirtshäuser:
            #print("Was Wirtshaus lautet:",wirtshaus)
            ort = models.Ortliste.objects.filter(name=ort_info.name)
            ortliste = get_object_or_404(models.Ortliste, pk=ort[0].id)
            models.Ort.objects.create(name=wirtshaus, typ="Wirtshaus", ortliste=ortliste)
            #print("Wirtshaus erfolgreich angelegt.")
        """
        for specialperson in ort_info.besondere_personen:
            print("Name der besonderen Person:",specialperson["name"])
            print("Rolle:",specialperson["rolle"])
            print("Beschreibung:",specialperson["beschreibung"])
            print("Plotansatz:",specialperson["plotansatz"])
            print("Anzutreffen in:",specialperson["besonderen_orte"],"mit dem Typ:",type(specialperson["besonderen_orte"]))
            try:
                print("HIER")
                figurenliste = get_object_or_404(models.Figurenliste, name="Nichtspieler Charaktere")
                print("HIER2:",figurenliste)
                ort = get_object_or_404(models.Ort, name=specialperson["besonderen_orte"])
                print("LISTE NSC GIBT ES !!!!!",figurenliste)
                models.Figur.objects.create(name=specialperson["name"], beruf=specialperson["rolle"], plot=specialperson["plotansatz"], figurenliste=figurenliste, kommentar="NSC", ort=ort)
            except:
                print("GIBT ES NICHT, ABER ICH LEGE SIE AN !!!!!")
                models.Figurenliste.objects.create(name="Nichtspieler Charaktere")
                print("Liste erfolgreich angelegt")
                figurenliste = get_object_or_404(models.Figurenliste, name="Nichtspieler Charaktere")
                print("Figurenliste abgerufen")
                ort = get_object_or_404(models.Ort, name=specialperson["besonderen_orte"])
                print("Ort erfolgreicha abgerufen")
                models.Figur.objects.create(name=specialperson["name"], beruf=specialperson["rolle"], plot=specialperson["plotansatz"], figurenliste=figurenliste, kommentar="NSC", ort=ort)
                print("Figur erfolgreich angelegt!")
        """
        return redirect ("ortliste")
    context = {"ortliste": ortliste}
    return render(request, "ortliste.html", context)

def ortliste_anlegen(request):
    models.Ortliste.objects.create(name=request.POST["ortliste_name"]) #request.POST überprüft vorher ob in dem Feld überhaupt was steht
    #listen_id = request.POST["ortliste_name"] #String in Integer umwandeln, damit es sauber weiterverarbeitet werden kann
    return redirect("ortliste")

def delete_ortliste(request, ort_id):
  schauplatz = models.Ortliste.objects.get(id=ort_id)
  schauplatz.delete()
  return redirect('ortliste')

def schauplatz(request, schauplatz_id):
    schauplatz_alle = get_object_or_404(models.Ort, pk=schauplatz_id)
    schauplatz = models.Schauplatz.objects.all()
    location = models.Schauplatz.objects.filter(ortliste=schauplatz_id)
    figuren = models.Figur.objects.filter(ort=schauplatz_id)
    figurenlisten = models.Figurenliste.objects.all()
    context = {"schauplatz": schauplatz, "schauplatz_alle": schauplatz_alle, "location": location, "figuren": figuren, "figurenlisten": figurenlisten}
    return render(request, "schauplatz.html", context)

def schauplatz_anlegen(request):
    ortliste = get_object_or_404(models.Ortliste, pk=request.POST["schauplatz_ort"]) #schauplatz_ort = Ausgewälter Ort aus Liste an Orten zB Albershausen
    models.Ort.objects.create(name=request.POST["schauplatz_name"], ortliste=ortliste) #schauplatz_name = input
    ortlisten_id = int(request.POST["schauplatz_ort"]) #String in Integer umwandeln, damit es sauber weiterverarbeitet werden kann
    return redirect("orte", ortlisten_id)

def delete_schauplatz(request):
  if request.method == 'POST':
        parameter1 = request.POST.get('parameter1')
        ortlisten_id = request.POST.get('parameter2')
  schauplatz = models.Ort.objects.get(id=parameter1)
  schauplatz.delete()
  return redirect('orte', ortlisten_id)

def location(request, location_id):
    location_alle = get_object_or_404(models.Schauplatz, pk=location_id)
    #location = models.Location.objects.all()
    context = {"location": location, "location_alle": location_alle}
    return render(request, "location.html", context)

def location_anlegen(request):
    schauplatzliste = get_object_or_404(models.Ort, pk=request.POST["parameter1"]) #schauplatz_ort = Ausgewälter Ort aus Liste an Orten zB Krissis Bude
    models.Schauplatz.objects.create(name=request.POST["location_name"], ortliste=schauplatzliste) #schauplatz_name = input
    schauplatz_id = int(request.POST["parameter1"]) #String in Integer umwandeln, damit es sauber weiterverarbeitet werden kann
    return redirect("schauplatz", schauplatz_id)

def location_edit(request, location_id):
    location_alle = get_object_or_404(models.Schauplatz, pk=location_id) 
    location = location_id
    if request.POST: 
        location_alle.raumtyp = request.POST["raumtyp"]
        location_alle.einrichtungsstil = request.POST["einrichtungsstil"]
        location_alle.beleuchtung = request.POST["beleuchtung"]
        location_alle.zustand = request.POST["zustand"]
        location_alle.nutzung = request.POST["nutzung"]
        location_alle.spezielle_gegenstände = request.POST["spezielle_gegenstände"]
        location_alle.gefahren_und_bedrohungen = request.POST["gefahren_und_bedrohungen"]
        location_alle.geheimnisse_und_versteckte_elemente = request.POST["geheimnisse_und_versteckte_elemente"]
        location_alle.quests_und_interaktionsmöglichkeiten = request.POST["quests_und_interaktionsmöglichkeiten"]
        location_alle.alive = "ort_alive" in request.POST
        location_alle.kommentar = request.POST["kommentar"]
        location_alle.save()
        return redirect('location', location_id)
    context = {"location": location, "location_alle": location_alle}
    return render(request, "location_edit.html", context)

def delete_location(request):
  if request.method == 'POST':
        parameter1 = request.POST.get('parameter1')
        schauplatz_id = request.POST.get('parameter2')
  schauplatz = models.Schauplatz.objects.get(id=parameter1)
  schauplatz.delete()
  return redirect('schauplatz', schauplatz_id)
