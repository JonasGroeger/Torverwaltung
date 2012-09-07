from django.shortcuts import render_to_response
from Froschbachtal.settings import PROJECT_DIR, MEDIA_ROOT, TEMPLATE_DIRS, DATABASE

def test(request):
    return render_to_response(
        'index.html', dict(project=PROJECT_DIR, media=MEDIA_ROOT, template=TEMPLATE_DIRS, db=DATABASE)
    )