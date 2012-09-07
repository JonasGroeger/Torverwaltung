from fabric.api import local

APP_NAME = "Torverwaltung"
YAML_FIXTURES = ["spieler", "mannschaft", "gegner"]
FIXTURES_FOLDER = "fixtures/"

def commit(msg):
    local('git add -A . && git commit -m "' + msg + '"')
    local('git push origin master')


def _db_import_data():
    fixture_string = " ".join(FIXTURES_FOLDER + str(x) + ".yaml" for x in YAML_FIXTURES)
    local('./manage.py loaddata ' + fixture_string)


def _db_clear_data():
    local('./manage.py sqlclear ' + APP_NAME)


def dbreset():
    """
    Deletes the db contents and loads the specified fixtures (imitial data) in the db
    """
    _db_clear_data()
    _db_import_data()

def server():
    """
    Starts a server for the application at localhost:8000
    """
    local('./manage.py runserver')
