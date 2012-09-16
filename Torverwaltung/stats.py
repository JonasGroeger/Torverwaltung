# coding=utf-8
from datetime import date
from Torverwaltung.models import Einsatz, Spieler

__author__ = 'Jonas Gröger'

def _einsaetze_zeitraum(spieler, from_date, to_date):
    # Einsaetze des Spielers holen
    sp_einsaetze = Einsatz.objects.filter(spieler=spieler)
    # Einsaetze im Zeitraum [from_date, to_date] filtern
    sp_einsaetze_zeitraum = [einsatz for einsatz in sp_einsaetze
                             if einsatz.spiel.datum.__ge__(from_date) and einsatz.spiel.datum.__le__(to_date)]
    return sp_einsaetze_zeitraum


def _mannschaften_zeitraum(sp_einsaetze_zeitraum):
    mannschaften_zeitraum = set()
    # Alle Mannschaften des Zeitraums filtern
    for e in sp_einsaetze_zeitraum:
        mannschaften_zeitraum.add(e.spiel.mannschaft)
    return mannschaften_zeitraum


def _tore_pro_mannschaft_zeitraum(mannschaften_zeitraum, sp_einsaetze_zeitraum):
    tore_mannschaft_zeitraum = list()
    for m in mannschaften_zeitraum:
        tore_zeitraum_in_m = sum([eins.tore for eins in sp_einsaetze_zeitraum if eins.spiel.mannschaft == m])
        s = MannschaftTore(tore_zeitraum_in_m, m)
        tore_mannschaft_zeitraum.append(s)

    # Sort by teamname
    tore_mannschaft_zeitraum.sort(key=lambda m: m.mannschaft.name)
    return tore_mannschaft_zeitraum


def _spieler_by_pk(spieler_pk):
    return Spieler.objects.get(pk=spieler_pk)


def _spieler_stats_r(spieler_pk, from_date, to_date):
    """
    Returns a list of MannschaftTore that describes the goals per team for that player in the specified time range.
    """

    # Spieler holen
    sp = _spieler_by_pk(spieler_pk)
    # Einsaetze des Spielers im Zeitraum holen
    sp_einsaetze_zeitraum = _einsaetze_zeitraum(sp, from_date, to_date)
    # Mannschaften der Einsaetze des Spielers im Zeitraum holen
    mannschaften_zeitraum = _mannschaften_zeitraum(sp_einsaetze_zeitraum)
    # Tore pro Mannschaft der Einsaetze des Spielers im Zeitraum holen
    tore_mannschaft_zeitraum = _tore_pro_mannschaft_zeitraum(mannschaften_zeitraum, sp_einsaetze_zeitraum)

    return tore_mannschaft_zeitraum


def _spieler_stats(spieler_pk, from_date, to_date):
    vor_langer_langer_zeit = date.min
    vorher = _spieler_stats_r(spieler_pk, vor_langer_langer_zeit, from_date)
    zeitraum = _spieler_stats_r(spieler_pk, from_date, to_date)

    return SpielerStats(_spieler_by_pk(spieler_pk), from_date, to_date, vorher, zeitraum)


def tore_pro_mannschaft_im_zeitraum(from_date, to_date):
    """
    Returns a list of SpielerStats containing a single row in the stats output
    """
    alle_spieler = Spieler.objects.all()

    alle_spieler_stats = list()
    for spieler in alle_spieler:
        spieler_stat = _spieler_stats(spieler.pk, from_date, to_date)
        alle_spieler_stats.append(spieler_stat)

    # Sort by player pk
    alle_spieler_stats.sort(key=lambda spieler_stat: spieler_stat.spieler.pk)
    return alle_spieler_stats


class SpielerStats(object):
    def __init__(self, spieler, from_date, to_date, tore_vorher_list, tore_zeitraum_list):
        self.spieler = spieler
        self.from_date = from_date
        self.to_date = to_date
        self.tore_vorher_list = tore_vorher_list
        self.tore_zeitraum_list = tore_zeitraum_list


class MannschaftTore(object):
    def __init__(self, tore, mannschaft):
        self.tore = tore
        self.mannschaft = mannschaft

    def __unicode__(self):
        return u'%d Tore mit %s'.format(self.tore, self.mannschaft)