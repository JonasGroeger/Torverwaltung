from django.shortcuts import render_to_response
from Froschbachtal.settings import PROJECT_DIR, MEDIA_ROOT, TEMPLATE_DIRS, DATABASE
from datetime import date
from Torverwaltung.stats import tore_pro_mannschaft_im_zeitraum

def stats_players(request):
    # Erstmal dummy daten laden :)
    from_d = date(2012, 1, 1)
    to_d = date(2012, 12, 31)
    alle_spieler_stats = tore_pro_mannschaft_im_zeitraum(from_d, to_d)

    return render_to_response(
        'statistik_alle_spieler.html', dict(spieler_stats_list=alle_spieler_stats)
    )


def test(request):
    return render_to_response(
        'index.html', dict(project=PROJECT_DIR, media=MEDIA_ROOT, template=TEMPLATE_DIRS, db=DATABASE)
    )