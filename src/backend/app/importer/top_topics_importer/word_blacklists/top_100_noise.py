TOP_100_NOISE = set(
    [
        # noise 2023
        'Übereinkommen',
        'Bekämpfung',
        'Feststellung',
        'Stand',
        'Anforderungen',
        'Bundesrepublik',
        'Begrüßung',
        'Unterrichtung',
        'Mrd',
        'Vereinbarung',
        'Bundestagsdrucksache',
        'Länder',
        'Vorschriften',
        'Ratsdok.',
        'Kommission',
        'Stärkung',
        'Jahre',
        'Verzicht',
        'Erleichterung',
        'Jahr',
        'Bund',
        'Mio',
        'Sozialausschuss',
        'Mitteln',
        'Verteidigung',
        'Maßnahmen',
        'Steigerung',
        'Anlagen',
        'Entscheidung',
        'Ergänzung',
        'Finanzierung',
        'Robert',
        'Festlegung',
        'Anhebung',
        'Reduzierung',
        'Bundesregierung,',
        'Bewertung',
        'Beschluss',
        'Übertragung',
        'Ordnungsrufes',
        'Zustimmung',
        'Lage',
        'Grundlage',
        'Mitgliedstaaten',
        'BT-Drs',
        'Unternehmen',
        'Möglichkeit',
        'Beteiligung',
        'Bundesminister',
        'Indikativen',
        'Vermeidung',
        'Einrichtung',
        'Namen',
        'EUZBBG',
        'Kosten',
        'Sammelübersicht',
        'Europa',
        'Berücksichtigung',
        'Daten',
        'Internationalen',
        'Prüfung',
        'Absatz',
        'Stellungnahme',
        'Beibehaltung',
        'Einfügung',
        'Anpassungen',
        'Antwort',
        'Bundesministerin',
        'Recht',
        'Prozent',
        'Personen',
        'Klarstellung',
        'WP',
        'Aufnahme',
        'Gesetz',
        'Aufhebung',
        'Richtlinie',
        'GESTA',
        'Modernisierung',
        'Ermöglichung',
        'Wann',
        'Auswirkungen',
        'BvR',
        'Rahmen',
        'Bezug:',
        'Ende',
        'Schaffung',
        'Vorschlag',
        'Verordnungsermächtigung',
        'Bundesministeriums',
        'Informationen',
        'Kenntnis',
        'Gesetzes',
        'Beschlusses',
        'Erteilung',
        'Titeländerung',
        'Hintergrund',
        'Förderung',
        'Sozial',
        'Zusammenhang',
        'Schutz',
        'Einhaltung',
        'Menschen',
        'Sondervermögens',
        'Olaf',
        'Neufassung',
        'Entschließung',
        'EU',
        'Vorlage',
        'Bereich',
        'Verwendung',
        'Entlastung',
        'Nutzung',
        'Originaltext',
        'Änderungen',
        'Bundestages',
        'Ländern',
        'Aufbau',
        'Anwendung',
        'Kommunen',
        'Wie',
        'Gemeinsamer',
        'Gesetzen',
        'Bundesministerium',
        'Höhe',
        'Union',
        'Rat,',
        'Arbeit',
        'Sicherheit',
        'Rechtsverordnungen;',
        'Ausgaben',
        'Wirtschafts-',
        'Staaten',
        'Koalitionsvertrag',
        'Wahl',
        'Europäische',
        'Verlangen',
        'Mitteilung',
        'Verbesserung',
        'Ausschuss',
        'Verpflichtung',
        'Sicht',
        'Europäischen',
        'Zusammenarbeit',
        'Petitionsausschusses',
        'Auffassung',
        'Fortsetzung',
        'Rat',
        'EP',
        'Regelung',
        'Parlament,',
        'Vorschau',
        'Gewährleistung',
        'AG',
        'Deutschen',
        'Abgabe',
        'Rechts',
        'Reform',
        'Frage',
        'Investitionen',
        'Jahren',
        'Hinblick',
        'Bereitstellung',
        'Parlaments',
        'Regelungen',
        'Aussprache',
        'Anlage',
        'Siehe',
        'Erweiterung',
        'Anträge',
        'Folgeänderungen',
        'Empfehlung',
        'Änderung',
        'Verfahren',
        'Vorlage,',
        'Regionen',
        'Vorhaben',
        'Bundesregierung',
        'br',
        'Republik',
        'Gesetzentwurf',
        'Klarstellungen',
        'Bundes',
        'Deutschland',
        'Verlängerung',
        'Angabe',
        'Ausschusses:',
        'Pflicht',
        'Anzahl',
        'Fraktion',
        'Deutschlands',
        'Erhöhung',
        'Buch',
        'Erneute',
        'Durchführung',
        'Versorgung',
        'Deutsche',
        'Mittel',
        'Sicherstellung',
        'Euro,',
        'Anpassung',
        'Parlament',
        'Petitionen',
        'Richtlinien',
        'Übereinkommens',
        'Verordnung',
        'Einsatz',
        'Bezug',
        'Abg',
        'Rates',
        'Zusätzliche',
        'Verhinderung',
        'Annahme',
        'Bundestag',
        'Unterstützung',
        'Sicherung',
        'Ausweitung',
        'Zugang',
        'Mitglieder',
        'Weiterentwicklung',
        'Ausbau',
        'Beendigung',
        'EuB-BReg',
        'Entwicklung',
        'Einführung',
        'Umsetzung',
        'Beschleunigung',
        'Bundeshaushalt',
        'Evaluierung',
        'Hat',
        'Vorgaben',
        'Bundesministers',
        'Standards',
        'Forschung',
        'Anerkennung',
        'Status',
        'Bericht',
        'Verbot',
        'Euro',
        'Fragestunde',
        'Entschließungsantrag',
        'Absenkung',
        # noise 2022
        "Debatte",
        "Mögliche",
        "Schlussfolgerungen",
        "Verordnungen",
        "Erlass",
        "Instrument",
        "Veröffentlichung",
        "Thema",
        "Entscheidungen",
        "Bewältigung",
        "Allgemeine",
        "Zahlen",
        "Vertrag",
        "Position",
        "Fonds",
        "Bereichen",
        "Staates",
        "GmbH",
        "Rechte",
        "Erklärung",
        "Erhalt",
        "Staat",
        "Historische",
        "Beschluss",
        "Petition",
        "Einrichtungen",
        "Erhebung",
        "Ergebnisse",
        "Plenarprotokoll",
        "Evaluation",
        "Begrenzung",
        "Beratung",
        "Einbeziehung",
        "Senkung",
        "Rahmenbedingungen",
        "Fall",
        "Errichtung",
        "Cent",
        "Zahl",
        "Folgen",
        "Abschaffung",
        "Wegfall",
        "Durchsetzung",
        "Zeitraum",
        "Betrieb",
        "Rechtsverordnung",
        "Artikel",
        "Einnahmen",
        "Monate",
        "Ausgestaltung",
        "Schriftliche",
        "Plant",
        "Regierungsvorlage",
        "Reformen",
        "Geschäftsordnung",
        "Behörden",
        "Entwurf",
        "Beginn",
        "Gemeinsamen",
        "Form",
        "Überprüfung",
        "Mündliche",
        "Fragen",
        "Ansicht",
        "Gebiet",
        "Vereinfachung",
        "Verschiebung",
        "Falle",
        "Wird",
        "Rahmenbedingungen",
        "Durchführungsbeschluss",
        "Abgeordneten",
        "Gewährleistungsermächtigungen",
        "Gründen",
        "Antrag",
        "Rechtsverordnungen",
        "Person",
        "Streichung",
        "Senkung",
        "Inanspruchnahme",
        "Innern",
        "Frauen",
        "Bürger",
        "Teil",
        "Ziele",
        "Meldung",
        "Konsequenzen",
        "Verhandlungen",
        "Mitglied",
        "Beschränkung",
        "Bestimmung",
        "Reaktion",
        "Inkrafttreten",
        "Bevölkerung",
        "Erkenntnisse",
        "Ausnahmen",
        "Ausschreibungen",
        "Streichung",
        "Ermächtigung",
        "Angaben",
        "Umfang",
        "Ziel",
        "Nachfolger",
        "Projektion",
        "Definition",
        "Land",
        "Bürgerliches",
        'Fraktionen',
        'Bundesamt',
        'Zuständigkeit',
        'Bundesamtes',
        'Zeitpunkt',
        'Seite',
        'Bestimmungen',
        'Streichung',
        'Ermächtigung',
        'Leistungen',
        'Angaben',
        'Umfang',
        'Ziel',
        'Nachfolger',
        'Neuregelung',
        'Bürgerliches',
        'Erstellung',
        'Einschätzung',
        'Aufgaben',
        'Inwiefern',
        'Warum',
        # noise 2021
        # parties
        'AFD',
        'SPD',
        'CDU',
        'CSU',
        'BÜNDNIS',
        'GRÜNEN',
        'LINKEN',
        'FDP',
        # times
        'Januar',
        'Februar',
        'März',
        'April',
        'Mai',
        'Juni',
        "August",
        'Juli',
        'September',
        'Oktober',
        'November',
        'Dezember',
        "Erstes",
        "Zweites",
        "Drittes",
        "Viertes",
        "Fünftes",
        "Sechstes",
        "Siebtes",
        "Achtes",
        "Neuntes",
        "Zehntes",
        "Elftes",
        "Zwölftes",
        "Ersten",
        "Zweiten",
        "Dritten",
        "Vierten",
        "Fünften",
        "Sechsten",
        "Siebten",
        "Achten",
        "Neunten",
        "Zehnten",
        "Elften",
        "Zwölften",
        "Erster",
        "Zweiter",
        "Dritter",
        "Vierter",
        "Fünfter",
        "Sechster",
        "Siebter",
        "Achter",
        "Neunter",
        "Zehnter",
        "Elfter",
        "Zwölfter",
        'Ausführung',
        'Darfur',
        'Erörterungstermin',
        'Luis',
        'Volumen',
        'Eröffnung',
        'Antrags',
        'Gutachten',
        'Sprecher',
        'Zeki',
        'Umleiten',
        'Staatliche',
        'Fortschritte',
        'Billigung',
        'Sitz',
        'Einkommen',
        'Fällen',
        'Table',
        'Karin',
        'Mehr',
        'Herbeirufung',
        'Jahresbericht',
        'Allgemeinverfügung',
        'Themen',
        'Meinung',
        'Vereinbarkeit',
        'Informationsmittel',
        'Gesetzesantrag',
        'Gute',
        'Offenlegung',
        'Behinderungen',
        'Abmilderung',
        'Vollmer',
        'Kann',
        'Border',
        'Personenkreis',
        'Verantwortung',
        'Faeser',
        'Brief',
        'Artikels',
        'Gesetzentwurfs',
        'Abschnitt',
        'GUARDIAN',
        'Entfristung',
        'Informationsaustausch',
        'Grid',
        'Vorlagepflichten',
        'Sitzverteilung',
        'Instituts',
        'Ferda',
        'Verhaltensregeln',
        'Vereinigungen',
        'Erstattung',
        'Übernahme',
        'Stiftung',
        'Bundesanstalt',
        'Durchschnittssatzes',
        'EUMPM',
        'Organisationen',
        'Smart',
        'Kenntnisse',
        'Ursprung',
        'Mitgliedern',
        'Vergleich',
        'Horizont',
        'Anfrage',
        'Vergaben',
        'Urenco',
        'Gemeinschaft',
        'Übermittlung',
        'Verfahrens',
        'Steuereinnahmen',
        'Präsidenten',
        'Notlage',
        'Yusuf',
        'Klara',
        'Festschreibung',
        'Stundung',
        'Wochen',
        'Information',
        'Zusammenführung',
        'Redezeit',
        'Accent',
        'Abschluss',
        'Präzisierung',
        'Protokolls',
        'Fristen',
        'Verhältnismäßigkeit',
        'Förderämter',
        'Ressorts',
        'Einzelplans',
        'Amts',
        'Verabschiedung',
        'Krall',
        'Ablehnung',
        'Geywitz',
        'Geschäftsordnungsantrag',
        'Kleinen',
        'Wahrung',
        'Gesetzesevaluation',
        'Monaten',
        'Gemeinsame',
        'Einklang',
        'Einschränkung',
        'Beeinträchtigung',
        'Diskussionen',
        'Qualität',
        'Kodex',
        'Effizienz',
        'Gesetzentwürfe',
        'Wege',
        'Ordnung',
        'Shading',
        'Commission',
        'Bundeskanzlerin',
        'Übrige',
        'Vereinigten',
        'Kooperation',
        'Wahlkreise',
        'Police',
        'Mission',
        'Maag',
        'Stellvertreter',
        'Strategische',
        'Ausgleich',
        'Stellen',
        'Kommunikationsmittel',
        'Aussage',
        'Parlamentarischen',
        'Barbe',
        'Hält',
        'Bundesländer',
        'Vorhaltung',
        'Institutes',
        'Hebner',
        'Mittleren',
        'Bundesländern',
        'Abfindungen',
        'Tätigkeit',
        'Kontrolle',
        'Sonderbericht',
        'Vorsitze',
        'Nachtrags',
        'Mitgefühl',
        'Themenfeldern',
        'Aufsicht',
        'Politik',
        'Aktionsplan',
        'Dauer',
        'Nachzug',
        'Öffentliche',
        'Erträgen',
        'Rosenbrock',
        'Hälfte',
        'Kleine',
        'Joint',
        'Begriffs',
        'Nichtberücksichtigung',
        'Genehmigung',
        'Geschäftsführung',
        'Festsetzung',
        'Interessen',
        'Vierteljahr',
        'Communication',
        'Strategiewechsel',
        'Anspruch',
        'Nationale',
        'Colorful',
        'Gebrauch',
        'Betroffene',
        'Genehmigungsverfahren',
        'Hinwirken',
        'Vereinbarte',
        'Betroffenen',
        'Resolution',
        'Abgeordnete',
        'Lasten',
        'Titel',
        'Teilnahme',
        'Kein',
        'Anhörung',
        'Geschäftsbereich',
        'Änderungsmaßgaben',
        'Prozessstoffs',
        'LAAYOUNE',
        'Aussetzung',
        'Melnyk',
        'Abschlussbericht',
        'Gewalt',
        'Personal',
        'Assessment',
        'Fünfundzwanzigstes',
        'BMDV',
        'European',
        'Gründe',
        'Gewährung',
        'Aufenthalten',
        'Ansehen',
        'Report',
        'Zwecke',
        'Bundesbehörden',
        'Berichtspflicht',
        'Prüfbehörde',
        'Region',
        'Konkretisierung',
        'Anhalten',
        'Verfügung',
        'Sofortige',
        'Gesetzesvollzug',
        'Verwaltungen',
        'Austausch',
        'Dokumentation',
        'Weiterer',
        'Engagement',
        'Risiken',
        'Agenturen',
        'Opfer',
        'Schäden',
        'David',
        'Behandlungen',
        'Wahrnehmung',
        'Inherent',
        'Gesamtstrategie',
        'Berichterstattung',
        'Methoden',
        'Sonderregelungen',
        'Bundeskanzler',
        'Gesetzesentwurfs',
        'Angelegenheiten',
        'Arbeitsweise',
        'Bürgerlichen',
        'Akteure',
        'Deals',
        'Märkte',
        'Bewilligungen',
        'Teilhabe',
        'Täuschung',
        'Nationalen',
        'Beirats',
        'Handlungsfelder',
        'Umgang',
        'LINKE',
        'Andrij',
        'Ersatz',
        'Aufklärung',
        'Geschäftsordnungen',
        'Treffen',
        'Drosten',
        'Nummer',
        'Swetlana',
        'List',
        'Schutzes',
        'Teilt',
        'Gegenzug',
        'Bundesebene',
        'Bestellung',
        'Anhängern',
        'Ebene',
        'Emergency',
        'Befreiung',
        'Remmers',
        'Sommer',
        'Abgaben',
        'Sozialgesetzbuch'

    ]
)
