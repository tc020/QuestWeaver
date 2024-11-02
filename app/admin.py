from django.contrib import admin

from . import models
from .models import Figur, Szene, Ort, Kapitel, Schauplatz


#admin.site.register(models.Szene)
#admin.site.register(models.Figur)
#admin.site.register(models.Ort)
#admin.site.register(models.Kapitel)
admin.site.register(models.Figurenliste)
admin.site.register(models.Ortliste)
admin.site.register(models.Schauplatz)


@admin.register(Szene) #ist dasselbe wie admin.site.register(Figur, FigurAdmin) nur eleganter
class SzeneAdmin(admin.ModelAdmin):
    fieldsets =(
            ('Erforderliche Informationen',{ #Angezeigter Text im Balken
                'description' : 'Diese Felder müssen ausgefüllt werden:', #Angezeigter Text über dem Formular
                'fields':('name',('kapitel','chronologie'),'ort') #Felder die angezeigt werden. Tupel = selbe Zeile
            }),
            ('Beschreibung der Szene',{ #Angezeigter Text für die Box
                'classes' : ('collapse',), #Ausklappbare Box
                'fields': ('beschreibung',) #enthaltenes Feld beschreibung aus models.Szene
            })            
    )
    list_display = ('name', 'kapitel', 'chronologie', 'ort') #Rubriken bei Auflistung
    list_filter = ('kapitel',) #liste lässt sich auch nach kapiteln filern und nur diese anzeigen   
    ordering =('name',) #liste wird sortiert nach name

@admin.register(Figur) 
class FigurAdmin(admin.ModelAdmin):
    fieldsets =(
            ('Erforderliche Informationen',{
                'description' : 'Diese Felder müssen ausgefüllt werden:',
                'fields':(('name','alive'))
            }),            
            ('Zusätzliche Informationen',{
                'description' : 'Für mehr Details können diese Felder ausgefüllt werden:',
                'fields':('geschlecht', 'beruf', 'rasse', 'figurenliste', 'ort')
            }),
    )
    list_display = ('name', 'alive', 'geschlecht', 'figurenliste')
    ordering =('name',)

@admin.register(Ort)
class OrtAdmin(admin.ModelAdmin):
    list_display = ('name', 'alive')
    ordering =('name',)

@admin.register(Kapitel)
class KapitelAdmin(admin.ModelAdmin):
    list_display = ('name', 'kapitelNr')
    ordering =('kapitelNr',)



