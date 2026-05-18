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
    ("alto / alta", "groß"),
    ("grosso / grossa", "kräftig"),
    ("grasso / grassa", "dick"),
    ("piccolo / piccola / basso / bassa", "klein"), # the last relate only to hight
    ("magro / magra", "dünn"),
    ("minuto / minuta", "zierlich"),
    ("snello / snella", "schlank"),
    ("assomigliare", "ähnlich"),
    ("assomigliarsi", "sich gleichen"),
    ("come", "so wie"),
    ("il capello", "das Haar / das Kopfhaar"),
    ("il pelo", "das Körperhaar"),
    ("la pettinatura", "die Frisur"),
    ("pettinare", "frisieren"),
    ("biondo / bionda", "blond"),
    ("castano / castana", "braunhaarig"),
    ("nero / nera", "schwarz"),
    ("rosso / rossa", "rot"),
    ("grigio / grigia", "grau"),
    ("moro / mora", "dunkelhaarig"), # auch Hautfarbe
    ("chiaro / chiara", "hell"),
    ("scuro / scura", "dunkel")
    ]

clothing = [
    ("l'abbigliamento", "die Kleidung"),
    ("la moda", "die Mode"),
    ("elegante", "elegant"),
    ("vestirsi", "sich anziehen"),
    ("mettersi", "anziehen"),
    ("portare", "tragen / anhaben"),
    ("togliersi", "ausziehen"),
    ("spogliarsi", "sich ausziehen"),
    ("cambiarsi", "such umziehen"),
    ("provare", "anprobieren"),
    ("stare", "stehen / passen"),
    ("il numero", "die Schuhgröße"),
    ("la taglia", "die Kleidergröße"),
    ("stretto / stretta", "eng"),
    ("largo / larga", "weit"),
    ("corto / corta", "kurz"),
    ("lungo / lunga", "lang"),
    ("la giacca", "die Jacke"),
    ("il cappotto", "der Mantel"),
    ("l'impermeabile", "die Regenjacke"),
    ("l'abito", "der Anzug / das Kleid"),
    ("il tailleur", "das Kostüm"),
    ("il vestito", "das Kleid"),
    ("i vestiti", "die Kleidung"),
    ("i pantaloni", "die Hose"),
    ("i pantaloncini", "die Shorts"),
    ("i jeans", "die Jeans"),
    ("la gonna", "der Rock"),
    ("la camicia", "das Hemd"),
    ("la camicetta", "die Bluse"),
    ("la maglia", "der Pullover"),
    ("la maglietta", "das T-Shirt"),
    ("la calza", "der Strumpf"),
    ("il calzino", "die Socke"),
    ("la scarpa", "der Schuh"),
    ("il pigiama", "der Schlafanzug"),
    ("la camicia da notte", "das Nachthemd"),
    ("il costume da bagno", "der Badeanzug / die Badehose"),
    ("le mutande", "der Slip / die Unterhose"),
    ("il bikini", "der Bikini")
    ]

accessory = [
    ("la borsa", "die Tasche"),
    ("la borsetta", "die Handtasche"),
    ("il portafoglio", "das Portmonnaie / der Geldbeutel / die Brieftasche"),
    ("il cappello", "der Hut / die Kappe"), # Achtung nur ein p ist das Haar
    ("il berretto", "die Mütze"),
    ("il guanto", "der Handschuh"),
    ("l'ombrello", "der Regenschirm"),
    ("l'anello", "der Ring"),
    ("l'orologio", "die Uhr"),
    ("la collana", "die Halskette"),
    ("l'orecchino", "der Ohrring"),
    ("gli occhiali", "die Brille"),
    ("gli occhiali da sole", "die Sonnenbrille")
    ]

family = [
    ("familiare", "familiär"),
    ("la famiglia", "die Familie"),
    ("i genitori", "die Eltern"),
    ("il padre", "der Vater"),
    ("il papà", "der Papa"),
    ("la madre", "die Mutter"),
    ("la mamma", "die Mama / die Mutti"),
    ("il figlio", "der Sohn"),
    ("la figlia", "die Tochter"),
    ("i figli", "die Kinder"),
    ("il fratello", "der Bruder"),
    ("la sorella", "die Schwester"),
    ("i fratelli", "die Geschwister"),
    ("lo zio", "der Onkel"),
    ("la zia", "die Tante"),
    ("il cugino", "der Cousin"),
    ("la cugina", "die Cousine"),
    ("il nonno", "der Großvater / der Opa"),
    ("la nonna", "die Großmutter / die Oma"),
    ("i nonni", "die Großeltern"),
    ("convivere", "zusammenleben"),
    ("occuparsi di", "sich kümmern um")
    ]

relationships_marriage = [
    ("l'amore", "die Liebe"),
    ("amare", "lieben"),
    ("amarsi", "sich lieben"),
    ("innamorato / innamorata", "verliebt"),
    ("innamorarsi", "sich verlieben"),
    ("voler bene a", "mögen"),
    ("l'odio", "der Hass"),
    ("odiare", "hassen"),
    ("il bacio", "der Kuss"),
    ("baciare", "küssen"),
    ("baciarsi", "sich küssen"),
    ("l'abbraccio", "die Umarmung"),
    ("abbracciare", "umarmen"),
    ("sposarsi", "heiraten"),
    ("il matrimonio", "die Hochzeit / die Trauung / die Ehe"),
    ("il marito", "der Ehemann"),
    ("la moglie", "die Ehefrau"),
    ("la coppia", "das Paar / das Ehepaar"),
    ("contrarre un'unione civile", "sich verpartnern"),
    ("l'unione civile", "die Lebenspartnerschaft"),
    ("fedele", "treu"),
    ("infedele", "untreu"),
    ("la separazione", "die Trennung"),
    ("separasi", "sich trennen")
    ]

friendships_and_social_contacts = [
    ("l'amicizia", "die Freundschaft"),
    ("l'amico", "der Freund"),
    ("l'amica", "die Freundin"),
    ("essere amici", "befreundet sein"),
    ("il giro di amici", "der Freundeskreis"),
    ("amichevole", "freundschaftlich"),
    ("personale", "persönlich"),
    ("la gente", "die Leute"), # only singular
    ("comune", "gemeinsam")
    ]

list_vocab_pairs_ital_deu = (personal_information
                             + character_traits
                             + appearance
                             + clothing
                             + accessory
                             + family
                             + relationships_marriage
                             + friendships_and_social_contacts
                             )
