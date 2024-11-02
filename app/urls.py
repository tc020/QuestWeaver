"""cicek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='homereal'),
    path('figuren', views.figuren, name='figuren'),
    path('ortliste', views.ortliste, name='ortliste'),
    path('orte/<int:ortlisten_id>', views.orte, name='orte'),
    path('orte_edit/<int:orte_id>', views.orte_edit, name='orte_edit'),
    path('ortliste_name', views.ortliste_anlegen, name='ortliste_anlegen'),
    path('schauplatz/<int:schauplatz_id>', views.schauplatz, name='schauplatz'),
    path('delete_ortliste/<int:ort_id>', views.delete_ortliste, name='delete_ortliste'),
    path('orte/delete_schauplatz', views.delete_schauplatz, name='delete_schauplatz'),
    path('schauplatz_name', views.schauplatz_anlegen, name='schauplatz_anlegen'),
    path('location/<int:location_id>', views.location, name='location'),
    path('location_edit/<int:location_id>', views.location_edit, name='location_edit'),
    path('location_name', views.location_anlegen, name='location_anlegen'),
    path('schauplatz/delete_location', views.delete_location, name='delete_location'),
    path('kapitel', views.kapitel, name='kapitel'),
    path('kapitel_name', views.kapitel_anlegen, name='kapitel_anlegen'),
    path('delete_kapitel/<int:kapitel_id>', views.delete_kapitel, name='delete_kapitel'),
    path('szenen/<int:szene_id>', views.szenen, name='szenen'),
    path('szene_anlegen', views.szene_anlegen, name='szene_anlegen'),
    path('szene_edit/<int:szeneedit_id>', views.szene_edit, name='szene_edit'),
    path('szenen/delete_szene', views.delete_szene, name='delete_szene'),
    path('listen/<int:listen_id>', views.listen, name='listen'),
    path('figurenliste_name', views.figurenliste_anlegen, name='figurenliste_anlegen'),
    path('listen/delete_figurenliste', views.delete_figurenliste, name='delete_figurenliste'),
    path('figur_name', views.figur_anlegen, name='figur_anlegen'),
    path('figuren_edit/<int:figuren_id>', views.figuren_edit, name='figuren_edit'),
    path('delete_figur/<int:figur_id>', views.delete_figur, name='delete_figur'),
    path('navbar', views.navbar, name='navbar'),
    path('header', views.header, name='header'),
    path('schauplatz_ebene2/<int:listen_id>', views.schauplatz_ebene2, name='schauplatz_ebene2'),
    #path('run-script/', views.run_script_view, name='run_script'),
]
