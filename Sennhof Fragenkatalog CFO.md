---
typ: Übung
projekt: Sennhof Schokolade
modul: Agentic Data Analytics
stand: 2026-10-03
---

# Sennhof: Datenlücken und Fragenkatalog an die CFO

Grundlage: Paket_1_Finanzen.zip (ER-Export, Umsatz nach Kunde/Artikel, MR August vorläufig, Rohstoffpreise, FTE, OP-Liste, Kampagnen, GL-Protokolle, Stammdaten, Sales-Dashboard). Alle Beträge in TCHF, Abweichung = Ist gegenüber Budget V3.

## 1. Was die Finanzdaten bereits belegen

| Befund | Zahl | Quelle |
|---|---|---|
| EBIT-Lücke ab Juni | Jun -191.3, Jul -180.9, Aug -149.1 (Aug vorläufig) | MR_08_26_vorl.xlsx, ER_2026_Monat |
| Überstunden/Temporäre Produktion | Jun bis Aug Mehraufwand 158.1 (Ist 53.5 / 67.1 / 50.9 statt rund 4.5 pro Monat), FTE Produktion stabil 117 bis 119 | ER-Export Konto 5050, FTE_Rep.csv |
| Retouren und Qualitätsgutschriften | Mai bis Aug Mehraufwand 143.5; Jun bis Aug 107.0 | ER-Export Konto 3810 |
| Retouren konzentriert auf Dunkel (TD70, TD85, TDO) | Retourenquote Dunkel Mai bis Aug 3.4 bis 5.3 % vom Brutto, Jan bis Apr 0.3 bis 0.7 %, übrige Produkte 0.0 bis 1.0 % | umsatz_kd_art_20260902.csv |
| Hauptbetroffener Kunde | FrischMarkt: Retouren rund 26 bis 28 pro Monat (Mai bis Jul); Dunkel-Menge Jul 8.5 t statt 12.2 t, Aug 8.2 t statt 13.0 t | umsatz_kd_art_20260902.csv |
| Materialverbrauch steigt bei stabilen Preisen | Materialaufwand / Standardkosten: Budget 1.021, Ist Jan bis Apr 1.02 bis 1.03, Jun 1.057, Jul 1.085, Aug 1.072 (rund 120 Mehraufwand Jun bis Aug) | ER-Export Konto 4000, stammdaten_art.csv |
| Kakao im oder unter Budget | Kakaomasse Jun bis Aug 11.37 / 11.48 / 11.60 CHF/kg (Budget 11.60), Kakaobutter 13.92 / 14.06 / 14.20 (Budget 14.20) | Preise RM 25-26.csv |
| Sommer 2025 ohne Auffälligkeit | Überstunden Jun bis Aug 2025: 5.1 / 6.2 / 3.9; Retouren 14.6 / 12.6 / 9.0 | ER-Export 2025 |
| Einmaleffekt IT | Juni +49.7 (ERP-Modul vorgezogen, Budget im September) | ER-Export Konto 6500, GL 14.04. |

**Zwischenstand zu den drei Vermutungen der GL**

* A Kakao: gegenüber Budget **nicht** belegt. Kakao ist zwar rund 20 % teurer als 2025, das ist aber budgetiert. Der Mehraufwand kommt aus der Menge (Verbrauch), nicht aus dem Preis.
* B Umsatz im Plan: nur **teilweise**. Brutto YTD +0.1 %, aber Netto YTD -125.4; Retouren und der Mengenrückgang Dunkel bei FrischMarkt sind ein Umsatzproblem. Das Dashboard verdeckt dies (Retourenquote YTD 1.0 %, Jun bis Aug rund 1.9 %).
* C Hitze: bisher **nicht** gestützt. Der Anstieg beginnt im Mai (vor dem Sommer), trifft fast nur Produkte der Linie L2 und trat im Sommer 2025 nicht auf. Endgültig prüfbar erst mit den Werksdaten.

## 2. Was fehlt

| Lücke | Warum sie wichtig ist |
|---|---|
| Ausschuss, Nacharbeit, Ausbeute pro Linie und Monat (2025 und 2026) | Einziger direkter Beleg für den Mehrverbrauch Material; Produktionsreport ("rückläufig") widerspricht dem Materialaufwand |
| Details zur Ersatzbeschaffung Osterpause | Zeitlicher Zusammenhang mit dem Beginn der Probleme ab Mai |
| Rezepturänderung Dunkel 85 % | Launch 04.05.2026, TD85 Retouren Mai 20.4 |
| Überstunden nach Linie und Grund | 158 Mehraufwand ohne Mehrmenge |
| Temperatur- und Klimadaten Werk 2025 und 2026 | Nötig, um die Hitze-Hypothese zu prüfen oder zu verwerfen |
| Reklamationsgründe der Kunden | Qualitätsursache (z. B. Fettreif, Bruch, Geschmack) |
| Lagerbestände und Inventur | Ob Materialaufwand Verbrauch oder Einkauf zeigt |
| Ergebnis Gespräch FrischMarkt 21.07. und Auslistungsumfang | Grösstes Risiko für Q4 |
| Hochrechnung Sep bis Dez | Für die VR-Frage "geht es weiter?" |
| Status Abschluss August | Aug ist vorläufig, Retouren Aug auffällig tiefer (31.7) |

## 3. Fragenkatalog an die CFO

Jede Frage nennt, was wir wissen wollen, was in den Daten uns dazu führt und welche Daten wir brauchen. Priorität 1 = für die VR-Aussage zwingend.

### Werk und Produktion

**F1 (Prio 1) Ersatzbeschaffung in der Osterpause**
* Frage: Welche Anlage wurde ersetzt, auf welcher Linie, durch welches Modell, und weshalb lag sie deutlich unter Budget?
* Datengrundlage: Unterhalt April 78.0 statt 115.0 (-37.0); GL 14.04. Punkt 2. Ab Mai steigen Retouren fast nur bei TD70, TD85, TDO, die ganz oder überwiegend auf L2 laufen (Stammdaten).
* Benötigt: Investitions- bzw. Bestellunterlagen, Inbetriebnahmedatum, Abnahmeprotokoll, Störungsprotokoll der Anlage.
* Hypothese wäre falsch, wenn: die Anlage nicht auf L2 steht oder die Fehlerrate auf L2 schon vor April anstieg.

**F2 (Prio 1) Ausschuss und Ausbeute pro Linie**
* Frage: Wie hoch waren Ausschuss, Nacharbeit und Ausbeute pro Linie und Monat 2025 und 2026, und aus welchem System stammt der Produktionsreport vor und nach dem 02.06.?
* Datengrundlage: Materialaufwand / Standardkosten steigt von 1.02 auf 1.085 (Jul) bei Kakaopreisen im Budget. Controlling (MR Kommentare Juni) und GL 14.07.: "Materialaufwand passt nicht zu den Produktionsmeldungen". ERP-Modul seit 02.06. live mit "Anzeigefehlern" (GL 16.06.).
* Benötigt: Produktionsreports L1 bis L4 monatlich, Rohdaten Ausschuss, Rohstoffverbrauch je Linie, Liste der fehlerhaften ERP-Reports.
* Hypothese wäre falsch, wenn: der Ausschuss auf L2 tatsächlich sinkt und der Mehrverbrauch anderswo entsteht.

**F3 (Prio 1) Überstunden**
* Frage: Auf welche Linien, Schichten und Gründe (Nacharbeit, Stillstand, Umrüsten, Mehrproduktion) entfallen die Überstunden und Temporären seit April?
* Datengrundlage: Konto 5050 Jun bis Aug 171.5 Ist gegen 13.5 Budget; FTE Produktion konstant 117 bis 119; Absatz unter Budget.
* Benötigt: Stundenrapporte bzw. Zeiterfassung nach Kostenstelle, Einsatzplan Temporäre.

**F4 (Prio 1) Hitze**
* Frage: Wie waren Raumtemperatur und Luftfeuchtigkeit in Produktion und Lager (insbesondere L2 und Kühltunnel) im Sommer 2025 und 2026, und gab es Klima- oder Kühlungsausfälle?
* Datengrundlage: Sommer 2025 ohne Anstieg bei Überstunden (5.1 / 6.2 / 3.9) und Retouren (14.6 / 12.6 / 9.0). Anstieg 2026 beginnt bereits im Mai und betrifft kaum Milch, Weiss und Pralinés.
* Benötigt: Temperaturprotokolle, Temperierkurven L2, Störmeldungen Kühlung.
* Hypothese "Hitze" wäre gestützt, wenn: 2026 deutlich heisser war und alle Linien gleich betroffen sind.

**F5 (Prio 2) Neue Rezeptur Dunkel 85 %**
* Frage: Was wurde an der Rezeptur geändert, ab welchem Datum wird sie produziert, und wurden Rohstoffe oder Prozessparameter auch für TD70 und TDO angepasst?
* Datengrundlage: Kampagne "Launch Dunkel 85 % neue Rezeptur" ab 04.05.2026; TD85 Retouren Mai 20.4 (Jan bis Apr 0.6 bis 4.0).
* Benötigt: Rezepturblatt alt und neu, Freigabeprotokoll QS.

**F6 (Prio 2) Reklamationsgründe**
* Frage: Welche Mängel nennen die Kunden bei den Retouren und Gutschriften (z. B. Fettreif, Bruch, Geschmack, Haltbarkeit), je Kunde, SKU und Charge?
* Datengrundlage: FrischMarkt Retouren Mai bis Jul 27.3 / 28.1 / 25.6; GL 14.07. "FrischMarkt unzufrieden mit Qualität Dunkel".
* Benötigt: Reklamationsprotokolle QS, Chargenrückverfolgung.

### Finanzen und Controlling

**F7 (Prio 1) Abgrenzung Materialaufwand**
* Frage: Zeigt Konto 4000 den Verbrauch nach Stückliste oder Einkäufe? Wie werden Lagerveränderungen und Ausschuss verbucht, und werden retournierte Waren vernichtet oder wiederverwertet?
* Datengrundlage: Materialaufwand pro kg 11.06 (Jan) bis 11.59 (Jul) bei stabilen Preisen.
* Benötigt: Lagerbestände Rohstoffe und Fertigwaren monatlich, letzte Inventur, Buchungslogik.

**F8 (Prio 2) Löhne Produktion**
* Frage: Sind die Löhne Produktion 2026 echte Ist-Werte?
* Datengrundlage: Konto 5000 entspricht in allen acht Monaten exakt dem Budget (Abweichung 0.0).
* Benötigt: Lohnjournal Produktion 2026.

**F9 (Prio 2) Abschluss August**
* Frage: Welche Positionen im August sind noch offen, insbesondere Retouren-Gutschriften und Materialabgrenzung?
* Datengrundlage: MR "vorläufig, Abschluss August noch nicht final"; Retouren August 31.7 deutlich unter Jun/Jul (49.6 / 48.0) trotz unveränderter Lage.
* Benötigt: Finaler Augustabschluss, Liste offener Gutschriften.

**F10 (Prio 3) Aktionsrabatte**
* Frage: Gibt es eine abgestimmte Liste der Aktionsrabatte pro Kunde und Monat?
* Datengrundlage: MR Zeile "Aktionsrabatte (Schätzung Verkauf, nicht abgestimmt)"; Dashboard meldet "Aktionen im Plan" ohne Beleg. Rabattquote FrischMarkt August 22.9 % (sonst rund 19 bis 21 %).
* Benötigt: Aktionskalender und Konditionen pro Kunde.

**F11 (Prio 1) Hochrechnung**
* Frage: Gibt es bereits eine Hochrechnung Sep bis Dez, und welche Annahmen enthält sie zu FrischMarkt und zu den Qualitätskosten?
* Datengrundlage: GL 14.04. "VR-Sitzung 29.09. mit Hochrechnung"; MR Kommentar August "Hochrechnung folgt nach Analyse".
* Benötigt: Hochrechnung bzw. Forecast-Version.

### Verkauf und Kunden

**F12 (Prio 1) FrischMarkt**
* Frage: Was war das Ergebnis des Gesprächs vom 21.07.? Welche Artikel sind von der angedrohten Auslistung betroffen, ab wann, und gibt es Bedingungen für den Verbleib?
* Datengrundlage: FrischMarkt Dunkel Nettoumsatz Sep bis Dez 2025: 1'927 (Saisonstärkstes Quartal); Dunkel-Menge Jul und Aug rund 35 % unter Budget; Bruttoumsatz FrischMarkt August -129.4 gegen Budget.
* Benötigt: Gesprächsnotiz, Korrespondenz, aktuelle Bestellprognose FrischMarkt Q4.

**F13 (Prio 3) NordImport DE**
* Frage: Welches Zahlungsziel und welche Kreditlimite gelten, und besteht eine Wertberichtigung (Delkredere)?
* Datengrundlage: DSO NordImport von 53.0 (Feb) auf 82.3 Tage (Aug); überfällig über 60 Tage 50.5 per August. Kein Delkredere-Konto in der ER. Liquiditätsthema, nicht Ursache der EBIT-Lücke.
* Benötigt: Debitorenstammdaten, Mahnstatus, Bonitätsauskunft.

### IT

**F14 (Prio 2) ERP-Modul Produktionsplanung**
* Frage: Welche Reports sind seit dem Go-live am 02.06. fehlerhaft, betrifft dies Ausschuss- oder Verbrauchsmeldungen, und hat sich die Planungslogik (Losgrössen, Reihenfolge, Umrüsten) geändert?
* Datengrundlage: GL 16.06. "Reports mit Anzeigefehlern"; Ausschuss laut Report "rückläufig", Materialverbrauch steigt.
* Benötigt: Ticketliste ERP, Vergleich Planungsparameter alt und neu.

## 4. Datenhygiene (für die Präsentation erwähnen)

* ER_Monat_2025-2026_final_v2.csv und "(1)" sind identisch, eine Datei genügt.
* umsatz_kd_art_20260815 ist vollständig in 20260902 enthalten (nur August neu, keine Änderungen an Vormonaten).
* Budget V2 (Entwurf) ist überholt, gültig ist Budget V3.
* ER-Export, Umsatzdatei und MR sind für 2026 abgestimmt (Brutto, Rabatte, Retouren stimmen auf 0.1 TCHF).
* Das Sales-Dashboard zeigt YTD-Werte, die den Einbruch ab Mai verwässern.
