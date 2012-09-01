from django.db import models

class Spieler(models.Model):
    vorname = models.CharField('Vorname', max_length=64)
    nachname = models.CharField('Nachname', max_length=64)
    geburtstag = models.DateField('Geburtstag')

    def __unicode__(self):
        return "%s %s (%s)" %\
               (self.vorname, self.nachname, self.geburtstag)


class Mannschaft(models.Model):
    name = models.CharField('Name der Mannschaft (z.B: Erste)', max_length=64)

    def __unicode__(self):
        return "%s" % (self.name)


class Spiel(models.Model):
    gegner = models.CharField('Name der gegnerischen Mannschaft', max_length=200)
    datum = models.DateField('Datum des Spiels')
    freundschaftsspiel = models.BooleanField('Freundschaftsspiel?')
    mannschaft = models.ForeignKey(Mannschaft)

    def __unicode__(self):
        return "%s gegen %s am %s mit Mannschaft %s" %\
               ('Freundschaftsspiel' if self.freundschaftsspiel else "Punktspiel", self.gegner, self.datum, self.mannschaft)


class Einsatz(models.Model):
    tore = models.PositiveIntegerField('Anzahl der Tore')
    spieler = models.ForeignKey(Spieler)
    spiel = models.ForeignKey(Spiel)

    def __unicode__(self):
        return "%d Tore von %s in %s" %\
            (self.tore, self.spieler, self.spiel)