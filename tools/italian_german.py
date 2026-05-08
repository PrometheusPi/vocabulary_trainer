personal_information = [
    ("l'uomo", "der Mann"),
    ("i uomini", "die Männer"),
    ("la donna", "die Frau"),
    ("il signor", "der Herr"),
    ("la signora", "die Frau"),
    ("la signorina", "die junge Frau"),
    ("il bebè", "das Baby"),
    ("il bambini", "der Junge / das Kind"),
    ("la bambina", "das Mädchen / das Kind"),
    ("il ragazzo", "der Junge"), # issue with Deu -> Ital ambiguous
    ("la ragazza", "das Mädchen"),
    ("chiamare", "nennen"),
    ("chimarsi", "heißen"),
    ("il nome", "der Vorname / der Name"),
    ("il cognome", "der Nachname"),
    ("sposato / sposata", "verheiratet"),
    ("celibe / nubile", "ledig / single"), # celibe only for males, nubile only for femals - how do I handle that?
    ("divorziato / divorziata", "geschieden"),
    ("vedovo / vedova", "verwitwet"),
    ("essere separato / essere separata", "gertennt leben"),
    ("venire da", "kommen aus"),
    ("essere di", "sein aus"),
    ("l'indirizzo", "die Adresse"),
    ("la città", "der Wohnort"), # how do distinguish this from "die Stadt"
    ("la via", "die Straße"),
    ("il numero (civico)", "die Hausnummer"),
    ("il numero di telefono", "die Telefonnummer"),
    ("il numero di cellulare", "die Handynummer"),
    ("maggiorenne", "volljährig"),
    ("minorenne", "minderjährig")
    ]

character_traits = [
    ("buono / buona", "gut / lieb"), # git Person
    ("bravo / brava", "gut / brav"), # gut Fähigkeit
    ("cattivo / cattiva", "schlecht"),
    ("gentile", "freundlich / nett / aufmerksam"),
    ("cordiale", "herzlich"),
    ("cortese", "höflich"),
    ("sgarbato / sgarbata", "unhöflich"),
    ("la pazienza", "die Geduld"),
    ("paziente", "geduldig"),
    ("impaziente", "ungeduldig"),
    ("prudente", "vorsichtig"),
    ("imprudente", "unvorsichtig"),
    ("serio / seria", "ernsthaft / ernst"),
    ("simpatico / simpatica", "sympatisch / nett"),
    ("antipatico / antipatica", "unsympathisch"),
    ("pigro / pigra", "faul"),
    ("allegro / allegra", "fröhlich / heiter / lustig"),
    ("comico / comica", "komisch"),
    ("depresso / depressa", "niedergeschlagen"),
    ("calmo / calma", "ruhig"),
    ("furbo / furba", "schlau"),
    ("la stupidità", "die Dummheit"),
    ("stupido / stupida", "dumm"),
    ("il coraggio", "der Mut"),
    ("coraggioso / coraggiosa", "mutig"),
    ("il vigliacco / la vigliacca", "der Feigling"),
    ("abituato / abituata", "gewöhnlich"),
    ("la personalità", "die Persönlichkeit"),
    ("il carattere", "der Charakter")
    ]

appearance = [
    ("l'aspetto", "das Aussehen"),
    ("sembrare", "aussehen"),
    ("carino / carina", "hübsch"),
    ("la bellezza", "die Schönheit"),
    ("bello / bella", "schön / gut  aussehend"), # wird wie bestimmter Artikel angepasst
    ("attraente", "attraktiv"),
    ("brutto / brutta", "hässlich"),
    ("la faccia", "das Gesicht"),
    ("la linea", "die Figur"),
    ("grande", "groß"), # wird zu gran vor Substantiven mit Vokal
    ]

list_vocab_pairs_ital_deu = personal_information + character_traits
