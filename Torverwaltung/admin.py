from Torverwaltung.models import Spieler, Mannschaft, Spiel, Einsatz, Gegner
from django.contrib import admin

class EinsatzInline(admin.TabularInline):
    model = Einsatz
    extra = 11

class SpielAdmin(admin.ModelAdmin):
    inlines = [EinsatzInline]
    list_filter = ['datum']
    search_fields = ['gegner__name']
    list_display = ('datum', 'gegner', 'mannschaft', 'freundschaftsspiel')

class SpielerAdmin(admin.ModelAdmin):
    list_display = ('vorname', 'nachname', 'geburtstag')

class GegnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MannschaftAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EinsatzAdmin(admin.ModelAdmin):
    list_filter = ['spieler']
    list_display = ('spieler', 'spiel', 'tore')

admin.site.register(Spieler, SpielerAdmin)
admin.site.register(Mannschaft, MannschaftAdmin)
admin.site.register(Gegner, GegnerAdmin)
admin.site.register(Spiel, SpielAdmin)
admin.site.register(Einsatz, EinsatzAdmin)