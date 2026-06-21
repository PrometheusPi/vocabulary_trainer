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
    ("comune", "gemeinsam"),
    ("il membro", "das Mitglied"),
    ("il vicino", "der Nachbar"),
    ("la vicina", "die Nachbarin"),
    ("il tipo", "der Typ / der Kerl"),
    ("vedersi", "sich treffen"),
    ("l'incontro", "die Begegnung / das Treffen"),
    ("incontrare", "treffen"),
    ("l'appuntamento", "die Verabredung"),
    ("darsi appuntamento", "sich verabreden"),
    ("partecipare", "teilnehmen"),
    ("invitare", "einladen"),
    ("andare a trovare", "besuchen"),
    ("l'ospite", "der Gast"),
    ("passare da", "vorbeikommen bei"),
    ("la conoscenza", "die Bekanntschaft"),
    ("il conoscente", "der Bekannte"),
    ("la conoscente", "die Bekannte"),
    ("il contatto", "der Kontakt"),
    ("contattare", "Kontakt aufnehmen mit")
    ]

life_cycle = [
    ("umano / umana", "menschlich"),
    ("l'essere umano", "der Mensch"),
    ("la vita", "das Leben"),
    ("vivo / viva", "lebendig"),
    ("vivere / essere vivo / essere viva", "leben"),
    ("la nascita", "die Geburt"),
    ("nascere", "geboren werden"),
    ("l'età", "das Alter"), # this collides with la vecchiaia - this mean any age
    ("avere ... anni", "... Jahre alt sein"),
    ("l'infanzia", "die Kindheit"),
    ("la gioventù", "die Jugend"),
    ("giovane", "jung"),
    ("l'adulto", "der Erwachsene / die Erwachsene"),
    ("adulto / adulta", "erwachsen"),
    ("la vecchiaia", "das Alter"), # this collides with l'età - this means old age
    ("vecchio / vecchia", "alt"),
    ("crescere", "wachsen / aufwachsen / großziehen"),
    ("la morte", "der Tod"),
    ("morto / morta", "tot"),
    ("mortale", "tödlich"),
    ("morire", "sterben"),
    ("perdere la vita", "ums Leben kommen"),
    ("il funerale", "die Beerdigung"),
    ("la tomba", "das Grab"),
    ("seppellire", "beerdigen"),
    ("cremare", "einäschern"),
    ("il lutto", "die Trauer"),
    ("il vedovo", "der Witwer"),
    ("la vedova", "die Witwe")
    ]

thoughts = [
    ("il pensiero", "der Gedanke"),
    ("pensare", "denken / nachdenken"),
    ("pensare di", "halten von"),
    ("il ricordo", "die Erinnerung"),
    ("ricordare", "erinnern / daran denken / wissen"),
    ("ricordarsi di", "sich erinnern an"),
    ("dimenticare / dimenticarsi di", "vergessen"),
    ("sembrare", "scheinen / glauben"),
    ("la speranza", "die Hoffnung"),
    ("sperare", "hoffen"),
    ("supporre", "annehmen / vermuten"),
    ("possibile", "möglich"),
    ("impossibile", "unmöglich"),
    ("forse", "vielleicht"),
    ("l'impressione", "der Eindruck"),
    ("considerare", "bedenken / abwägen"),
    ("immaginare / immaginarsi", "sich vorstellen / denken"),
    ("chiedersi", "sich fragen"),
    ("accorgersi", "bemerken"),
    ("aspettarsi", "erwarten / rechnen mit")
    ]

feelings = [
    ("il sentimento", "das Gefühl / die Empfindung"),
    ("provare", "empfinden"),
    ("la felicità", "das Glück"),
    ("felice", "glücklich"),
    ("infelice", "unglücklich"),
    ("l'allegria", "die Fröhlichkeit"),
    ("contento / contenta", "froh"),
    ("essere contento, essere contenta", "sich freuen"),
    ("la gioia", "die Freude"),
    ("il sorriso", "das Lächeln"),
    ("sorridere", "lächeln / anlächeln"),
    ("le risate", "das Lachen"),
    ("ridere", "lachen"),
    ("il piacere", "die Freude / der Gefallen"),
    ("piacere", "gefallen / mögen / gern tun"),
    ("piacevole", "angenehm"),
    ("spiacevole", "unangenehm"),
    ("dispiacere", "leid tun"),
    ("dispiacersi", "bedauern"),
    ("purtroppo", "leider"),
    ("preferito / preferita", "Lieblings- / bevorzugter / bevorzugte"),
    ("preferire", "lieber mögen / lieber tun"),
    ("non sopportare", "nicht leiden können"),
    ("essere stufo di / essere stufa di", "satthaben"),
    ("la sorpresa", "die Überraschung"),
    ("sorprendere", "überraschen / erstaunen"),
    ("soddisfatto / soddisfatta", "zufrieden"),
    ("insoddisfatto / insoddisfatta", "unzufrieden"),
    ("la paura", "die Angst"),
    ("preoccupato /preoccupata", "beunruhigt / besorgt"),
    ("preoccuparsi", "sich Sorgen machen"),
    ("la tristezza", "die Traurigkeit"),
    ("triste", "traurig"),
    ("solo / sola", "einsam / allein"),
    ("piangere", "weinen"),
    ("terribile", "schrecklich / furchtbar"),
    ("orribile", "scheußlich")
    ]

senses = [
    ("vedere", "sehen"),
    ("guardare", "ansegen / nachsehen"),
    ("l'occhiata", "der Blick"),
    ("sentire", "hören / fühlen / riechen"),
    ("il rumore", "das Geräusch / der Krach / der Lärm"),
    ("toccare", "berühren / anfassen"),
    ("l'odore", "der Geruch"),
    ("avere odore", "riechen / Geruch haben"),
    ("il profumo", "der Duft")
    ]

conversations = [
    ("il discorso", "das Gespräch / die Rede"),
    ("parlare", "sprechen / reden"),
    ("dire", "sagen"),
    ("raccontare", "erzählen"),
    ("chiamare", "rufen"),
    ("il silenzio", "die Stille / das Schweigen"),
    ("silenzioso / silenziosa", "schweigsam / still"),
    ("zitto / zitta", "still / ruhig")
    ]

questions = [
    ("chiedere", "fragen / bitten / fordern / verlangen"),
    ("pregare", "bitten"),
    ("la domanda", "die Frage / der Antrag"),
    ("la richiesta", "die Bitte / die Forderung"),
    ("Come?", "Wie bitte?"),
    ("Prego!", "Bitte!"),
    ("per favore", "bitte"),
    ("Potrebbe ...?", "Können Sie bitte ...?"),
    ("la risposta", "die Antwort"),
    ("rispondere", "antworten"),
    ("sì", "ja / doch"),
    ("no", "nein"),
    ("non", "nicht"),
    ("ringraziare", "danken / sich bedanken"),
    ("Grazie!", "Danke!"),
    ("Tante grazie!", "Vielen Dank!"),
    ("Grazie mille!", "Tausend Dank!"),
    ("Di niente!", "Keine Ursache!"),
    ("Non c'è di che!", "Gern geschehen!"),
    ("la promessa", "das Versprechen"),
    ("promettere", "versprechen"),
    ("la volontà", "der Wille"),
    ("volere", "wollen")
    ]

orders = [
    ("l'ordine", "der Befehl"),
    ("ordinare", "befehlen / anordnen"),
    ("il permesso", "die Erlaubnis"),
    ("permettere", "erlauben / gestatten / zulassen"),
    ("potere", "dürfen"),
    ("va bene", "in Ordnung"),
    ("il divieto", "das Verbot"),
    ("vietato / vietata", "verboten"),
    ("vietare", "verbieten / untersagen"),
    ("impedire di", "hindern an")
    ]

discussion = [
    ("l'opinione", "die Meinung"),
    ("il parere", "die Ansicht"),
    ("secondo me", "meiner Meinung nach"),
    ("il consiglio", "der Rat"),
    ("consigliare", "raten / empfehlen"),
    ("suggerire", "empfehlen"),
    ("proporre", "vorschlagen"),
    ("accettare", "annehmen / akzeptieren"),
    ("approvare", "zustimmen"),
    ("d'accordo", "einverstanden"),
    ("tollerare", "dulden / hinnehmen"),
    ("convinto / convinta", "überzeugt"),
    ("convincere", "überzeugen"),
    ("avere ragione", "Recht haben"),
    ("avere torto", "Unrecht haben"),
    ("chiaro / chiara", "klar"),
    ("evidente", "offensichtlich"),
    ("esatto / esatta", "genau"),
    ("l'importanza", "die Bedeutung / die Wichtigkeit"),
    ("importante", "wichtig"),
    ("la critica", "die Kritik"),
    ("criticare", "kritisieren"),
    ("cioè", "also / das heißt"),
    ("per esempio", "zum Beispiel"),
    ("contro", "gegen")
    ]

conflicts = [
    ("la lite", "der Streit"),
    ("litigare", "streiten"),
    ("la rabbia", "der Ärger / die Wut / der Zorn"),
    ("arrabbiato / arrabbiata", "böse / wütend"),
    ("arrabbiarsi", "sich aufregen"),
    ("fare arrabbiare", "ärgern"),
    ("disturbare", "stören"),
    ("prendersela", "übel nehmen"),
    ("la lamentela", "die Klage / die Beschwerde"),
    ("lamentarsi", "sich beschweren / sich beklagen / klagen")
    ]

greetings_leaving = [
    ("Buongiorno!", "Guten Tag! / Guten Morgen!"),
    ("Buonasera!", "Guten Abend!"),
    ("Buonanotte!", "Gute Nacht!"),
    ("Arrivederci!", "Auf Wiedersehen!"),
    ("Salve!", "Hallo! / Auf Wiedersehen!"),
    ("Ciao!", "Hallo! / Tschüss!"),
    ("Ci vediamo!", "Bis dann!"),
    ("Ci sentiamo!", "Wir hören voneinander!"),
    ("A dopo!", "Bis nachher!"),
    ("A presto!", "Bis bald!"),
    ("A domani!", "Bis morgen!"),
    ("Buona giornata!", "Einen schönen Tag!"),
    ("Buona serata!", "Einen schönen Abend!"),
    ("Benvenuto! / Benvenuta!", "Willkommen!"),
    ("Molto piacere!", "Sehr erfreut!"),
    ("Addio!", "Leb wohl! / Lebt wohl! / Leben Sie wohl!")
    ]

common_expression_phrases = [
    ("Come sta?", "Wie geht es Ihnen?"),
    ("Come stai?", "Wie geht es dir?"),
    ("Bene, grazie!", "Danke, gut!"),
    ("Avanti!", "Herein!"),
    ("Si accomodi!", "Kommen Sie herein! / Nehmen Sie doch Platz!"),
    ("Verrei ...", "Ich möchte ... / Ich hätte gerne ..."),
    ("Vorresti ...?", "Möchtest du ...?"),
    ("Vorrebbe ...?", "Möchten Sie ...?"),
    ("Si serva!", "Bedienen Sie sich!"),
    ("Serviti!", "Bedien dich! / Nimm dir!"),
    ("Sì, grazie!", "Ja, gern! / Ja, bitte!"),
    ("Ecco!", "Hier!"),
    ("Speriamo!", "Hoffentlich!"),
    ("Lo spero!", "Ich hoffe es!"),
    ("Spero di sì!", "Ich hoffe!"),
    ("Spero di no!", "Ich hoffe nicht!"),
    ("Cosa succede?", "Was ist los?"),
    ("Tutto bene!", "Alles klar!"),
    ("Non importa!", "Das macht nichts!"),
    ("Non c'è problema!", "Kein Problem!"),
    ("Non te la prendere!", "Mach dir nichts draus!"),
    ("Non se la prenda!", "Machen Sie sich nichts daraus!")
    ]

list_vocab_pairs_ital_deu = (personal_information
                             + character_traits
                             + appearance
                             + clothing
                             + accessory
                             + family
                             + relationships_marriage
                             + friendships_and_social_contacts
                             + life_cycle
                             + thoughts
                             + feelings
                             + senses
                             + conversations
                             + questions
                             + orders
                             + discussion
                             + conflicts
                             + greetings_leaving
                             + common_expression_phrases
                             )
