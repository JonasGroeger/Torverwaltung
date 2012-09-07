# coding=utf-8
from django.db import models

class Spieler(models.Model):
    vorname = models.CharField('Vorname', max_length=64)
    nachname = models.CharField('Nachname', max_length=64)
    geburtstag = models.DateField('Geburtstag')

    def __unicode__(self):
        return u'%s %s' % (self.vorname, self.nachname)


    class Meta:
        db_table = u'Spieler'
        verbose_name = db_table
        verbose_name_plural = db_table


class Mannschaft(models.Model):
    name = models.CharField('Name der Mannschaft', max_length=64)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = u'Mannschaft'
        verbose_name = db_table
        verbose_name_plural = db_table + u'en'


class Gegner(models.Model):
    name = models.CharField('Name der gegnerischen Mannschaft', max_length=200)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = u'Gegner'
        verbose_name = db_table
        verbose_name_plural = db_table


class Spiel(models.Model):
    datum = models.DateField('Datum des Spiels')
    freundschaftsspiel = models.BooleanField('Freundschaftsspiel?')
    mannschaft = models.ForeignKey(Mannschaft)
    gegner = models.ForeignKey(Gegner)

    def __unicode__(self):
        art = u'Freundschaftsspiel' if self.freundschaftsspiel else u'Punktspiel'
        return u'%s mit der %s gegen %s am %s' % (art, self.mannschaft, self.gegner, self.datum, )

    class Meta:
        db_table = u'Spiel'
        verbose_name = db_table
        verbose_name_plural = db_table + u'e'


class Einsatz(models.Model):
    tore = models.PositiveIntegerField('Anzahl der Tore', default=0)
    spieler = models.ForeignKey(Spieler)
    spiel = models.ForeignKey(Spiel)

    def __unicode__(self):
        return u'[%d Tore von %s im %s]' % (self.tore, self.spieler, self.spiel)

    class Meta:
        db_table = u'Einsatz'
        verbose_name = db_table
        verbose_name_plural = u'Einsätze'