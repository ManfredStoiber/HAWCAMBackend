Setup Backend 

Zun�chst Python installieren: https://www.python.org/downloads/

1. Branch feature_create_category aus Git herunterladen 
2. CMD �ffnen
3. zu <Pfad zu Dateien>HAWCAMBackend\venv\Scripts navigieren
4. .\activate ausf�hren
5. zur�ck zu HAWCAMBackend navigieren
6. Befehl: python controller.py 
7. Controller ist nun erreichbar unter
	localhost:5000/api/v1.0/createCategory     -> Kategorie anlegen
	localhost:5000/api/v1.0/listCategories     -> Kategorien auflisten

Achtung: "Kategorien auflisten" liefert im Moment nur Dummy-JSON zur�ck, da noch nicht weiter implementiert
Format des Dummy-JSONs:
{
    "categories": {
        "1": {
            "name": "Raum",
            "count": 3
        },
        "2": {
            "name": "Buch",
            "count": 14
        },
        "3": {
            "name": "Rechner",
            "count": 10
        }
    }
}

