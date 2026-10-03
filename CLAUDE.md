# Sennhof Schokolade: Analyseauftrag für Claude Code

## Auftrag
Die CFO (Nadia Rossi) muss dem Verwaltungsrat erklären, warum Sennhof seit Juni 2026 rund CHF 150 bis 190k pro Monat unter Budget liegt, ob es weitergeht und was zu tun ist. "Zahlen, keine Vermutungen." Ergebnis: Präsentation mit visualisierten Kernaussagen, jede Zahl belegbar. Ich (Rino) verantworte jede Zahl.

## Arbeitsregeln
1. Erkläre vor jedem Rechenschritt kurz, was du vorhast und warum. Danach: was du gelernt hast.
2. Rechnen, nicht raten. Jede Zahl entsteht aus einem Skript in `analyse/` und ist reproduzierbar.
3. Jede Aussage mit Beleg: Datei, Spalte/Konto, Periode, Wert.
4. Trenne strikt **belegt** und **vermutet**. Vermutungen als solche kennzeichnen.
5. Nenne zu jeder Hypothese, welcher Befund sie widerlegen würde, und prüfe ihn aktiv.
6. Rohdaten nie verändern. Bereinigte Daten nach `daten_bereinigt/`.
7. Beträge in TCHF, Abweichung = Ist gegenüber Budget V3. Budget V2 nicht verwenden.
8. Sprache Deutsch, Schweizer Schreibweise (ss), keine Gedankenstriche.
9. Bei Widersprüchen zwischen Quellen: nicht auflösen durch Annahme, sondern melden und als Frage an die CFO formulieren.

## Datenlandkarte
Paket 1 Finanzen (entpackt in `Paket_1_Finanzen/`):
* `Export_ERP/ER_Monat_2025-2026_final_v2.csv`: Erfolgsrechnung pro Konto und Monat, Ist 2025 bis Aug 2026, Budget 2026. Die Datei "(1)" ist identisch, ignorieren.
* `Export_ERP/umsatz_kd_art_20260902.csv`: Umsatz nach Kunde x SKU x Monat inkl. Rabatte, Retouren, Budgetmenge. Ersetzt `..._20260815` (nur August neu).
* `Controlling/MR_08_26_vorl.xlsx`: Monatsreporting August (vorläufig), Kommentare Controlling.
* `stammdaten_art.csv`: SKU, Linie(n), Listenpreis, Standard-Materialkosten pro kg.
* `Einkauf/Preise RM 25-26.csv`, `HR/FTE_Rep.csv`, `FiBu/OP_Liste_Debi_mtl.csv`, `FiBu/fx_eurchf.csv`, `Marketing/Kampagnen_Übersicht_MK.csv`, `GL/Protokolle GL 2026 (Auszug).md`.

Paket 2 Werk und Antworten CFO (wenn vorhanden, in `Paket_2_Werk/` und `CFO_Antworten.md`). Zuerst inventarisieren: was ist was, was gehört zusammen, was ist doppelt, alt oder unklar, was fehlt.

## Stand der Analyse (belegt aus Paket 1)
* EBIT-Abweichung: Jun -191.3, Jul -180.9, Aug -149.1 (Aug vorläufig).
* Treiber Jun bis Aug: Überstunden/Temporäre +158.2, Retouren +107.0, Material-Mehrverbrauch +132.8 nach Mengen-/Mix- und Kakaopreiseffekt (Material / Standardkosten 1.057 / 1.085 / 1.072 gegen Budget 1.021), Bruttoumsatz -135, IT Juni +49.7 (Einmaleffekt ERP-Go-live vorgezogen).
* Kakaopreise Jun bis Aug im oder unter Budget: Vermutung A (Kakao) gegenüber Budget nicht belegt.
* Retouren fast nur Dunkel (TD70, TD85, TDO, Linie L2), ab Mai; Hauptkunde FrischMarkt. Dunkel-Menge FrischMarkt Jul/Aug rund 35 % unter Budget. Vermutung B (Umsatz im Plan) nur teilweise richtig.
* Sommer 2025 ohne Anstieg bei Retouren und Überstunden; Anstieg 2026 beginnt im Mai. Vermutung C (Hitze) bisher nicht gestützt.
* Zeitliche Auffälligkeiten: Ersatzbeschaffung Produktion in Osterpause "deutlich unter Budget" (Unterhalt Apr -37), Rezeptur Dunkel 85 % neu ab 04.05., ERP-Produktionsplanung live 02.06. mit Reportfehlern.
* Risiko Q4: FrischMarkt Dunkel Nettoumsatz Sep bis Dez 2025 = 1'927 TCHF, Auslistung angedroht.
* Auffällig: Löhne Produktion 2026 jeden Monat exakt = Budget. NordImport DSO 53 auf 82 Tage (Liquidität, nicht EBIT).

## Arbeitshypothese (zu prüfen)
Eine Störung auf Linie L2 seit Ende April (Ersatzanlage und/oder neue Rezeptur) erzeugt Qualitätsmängel bei Dunkelschokolade. Folgen: mehr Ausschuss (Material), Nacharbeit (Überstunden), Retouren und Mengenverlust bei FrischMarkt. Der Produktionsreport zeigt dies nicht, weil das neue ERP-Modul den Ausschuss falsch ausweist.

Widerlegt, wenn: Ausschuss/Fehler auf L2 nicht höher als auf L1, L3, L4; Anstieg schon vor April; Werkstemperatur 2026 deutlich höher als 2025 und alle Linien gleich betroffen; Materialmehraufwand durch Lagerbuchungen statt Verbrauch erklärbar.

## Analyseschritte mit Paket 2
1. Inventar Paket 2 (Tabelle: Datei, Inhalt, Zeitraum, Qualität, Bezug zu Paket 1).
2. Ausschuss und Ausbeute je Linie und Monat 2025 bis 2026; Vergleich Produktionsreport alt/neu um den 02.06.
3. Mengenbilanz Material: Soll-Verbrauch (Menge x Standardkosten) gegen Ist, nach Linie; Lagerveränderung berücksichtigen.
4. Überstunden nach Linie und Grund; Bezug zu Ausschuss/Nacharbeit.
5. Temperatur 2025 gegen 2026 je Bereich; Korrelation mit Fehlerrate je Linie.
6. Reklamationsgründe je SKU, Kunde, Charge; Zuordnung zu Linie und Produktionsdatum.
7. Brücke EBIT Budget zu Ist Jun bis Aug (Wasserfall) mit belegten Ursachen; Rest ausweisen.
8. Hochrechnung Sep bis Dez in drei Szenarien (Problem behoben ab Okt / bleibt / FrischMarkt listet Dunkel aus), Annahmen offenlegen.
9. Massnahmen mit Wirkung in TCHF und Verantwortlichen.
10. Skeptiker-Check: zwei Kernzahlen zum Nachrechnen in Excel aufbereiten (Rechenweg, Quellzellen).

## Ausgabe
* `analyse/*.py` Skripte, `ergebnisse/*.csv` Zahlen, `grafiken/*.png` Charts
* `ergebnisse/belegliste.md`: jede Zahl der Präsentation mit Quelle
* `praesentation/`: 4-Minuten-Präsentation (max. 6 Folien): Was ist passiert und warum, geht es weiter und was kostet es, was tun wir jetzt; Anhang mit Belegen und offenen Punkten
* `ergebnisse/rueckfragen_cfo.md`: wahrscheinliche Rückfragen der CFO mit belegten Antworten
