---
typ: Übung
projekt: Sennhof Schokolade
stand: 2026-10-03
---

# Sennhof: Analyse mit den vorhandenen Daten

Basis: Paket 1 Finanzen und Antwort CFO zu F1 (Temperiermaschine L2). Werksdaten liegen noch nicht vor. Alle Beträge in TCHF, Abweichung = Ist gegenüber Budget V3. Skripte: `analyse/bruecke.py`, `analyse/grafiken.py`.

## 1. Was ist passiert? EBIT-Brücke Juni bis August

![[grafiken/1_ebit_bruecke.png]]

| Treiber | TCHF | Herleitung | Status |
|---|---|---|---|
| Überstunden/Temporäre Produktion | -158.2 | Konto 5050, Ist minus Budget | belegt |
| Material-Mehrverbrauch | -132.8 | Konto 4000 minus Mengen-/Mixeffekt (+55.3) minus Kakaopreiseffekt (+11.3) | belegt (Rechnung), Ursache vermutet |
| Retouren und Qualitätsgutschriften | -107.0 | Konto 3810 | belegt |
| Umsatz/Mix | -67.2 | Bruttoumsatz -135.0, Rabatte +12.5, Mengen-/Mixeffekt Material +55.3. Dunkel -309 Brutto, übrige +174 | belegt |
| IT ERP (einmalig) | -48.0 | Konto 6500, v. a. Juni +49.7, Go-live vorgezogen (Budget September) | belegt, Timing |
| Übrige (Energie, Logistik, Unterhalt, Marketing) | -19.5 | | belegt |
| Kakaopreis | +11.3 | Kakaomasse/-butter Ist unter Budget, gewichtet mit Kakaoanteil aus Stammdaten | belegt (Näherung) |
| **EBIT-Abweichung Jun bis Aug** | **-521.4** | Jun -191.3, Jul -180.9, Aug -149.1 | Aug vorläufig |

Überstunden, Mehrverbrauch und Retouren ergeben zusammen **398 TCHF, rund drei Viertel der Lücke**. Alle drei springen im Mai.

## 2. Warum? Die Spur führt zu Linie 2

![[grafiken/2_retouren_dunkel.png]]

![[grafiken/3_material_ueberstunden.png]]

**Belegt**
* 06.04.2026: Auf Linie 2 wurde die Temperiermaschine durch das günstigere Drittanbieter-Modell TX-200 statt der Originalmaschine KT-900 ersetzt (Einsparung CHF 38'000, Entscheid Einkauf). Das stimmt mit Unterhalt April überein (Ist 78.0, Budget 115.0).
* Retourenquote Dunkel (TD70, TD85, TDO, alle Linie 2) springt von 0.3 bis 0.7 % (Jan bis Apr) auf 3.4 bis 5.3 % (Mai bis Aug). Übrige Produkte bleiben bei 0.0 bis 1.0 %.
* Mai bis August entfallen 67 bis 99 % aller Retouren auf Dunkel.
* Der Material-Mehrverbrauch steigt von 1 bis 13 pro Monat (Jan bis Apr) auf 25, 39, 52, 41 (Mai bis Aug).
* FrischMarkt bestellt weniger Dunkel: Juli -3.7 t, August -4.9 t gegen Budget. Andere Kunden kaum verändert.
* Die Kakaopreise liegen Mai bis Aug im oder unter Budget.

**Vermutet (noch nicht belegt)**
* Die TX-200 temperiert die Dunkelschokolade nicht stabil. Dunkelschokolade mit hohem Kakaobutteranteil hat ein enges Temperierfenster; Folgen wären Fettreif, Ausschuss und Nacharbeit. Belegt wäre dies erst mit Ausschussdaten L2, Reklamationsgründen und Temperierprotokollen.
* Der Produktionsreport zeigt sinkenden Ausschuss, weil das ERP-Modul seit 02.06. falsch rapportiert.

## 3. Die drei Vermutungen der Geschäftsleitung

| | Vermutung | Urteil | Beleg |
|---|---|---|---|
| A | Kakao frisst die Marge | **Nein** (gegenüber Budget) | Kakaopreiseffekt Jun bis Aug +11.3, also günstiger als geplant. Gegenüber 2025 ist Kakao zwar rund 20 % teurer, das ist aber budgetiert. |
| B | Umsatz im Plan, Problem sind die Kosten | **Teilweise** | Brutto YTD +0.1 %, aber Retouren -107 und Dunkel-Umsatz -309 Jun bis Aug; Netto und Mix sind ein Umsatzproblem. Das Dashboard (Retourenquote YTD 1.0 %) verdeckt es. |
| C | Heisser Sommer | **Nicht gestützt** | Anstieg beginnt im Mai, betrifft nur Linie 2, Sommer 2025 ohne Effekt (Überstunden 5.1 / 6.2 / 3.9; Retouren 14.6 / 12.6 / 9.0). Hitze kann die schwächere Maschine zusätzlich belasten (offen, F4). |

## 4. Geht es weiter, und was kostet es?

![[grafiken/4_ausblick.png]]

| Szenario Sep bis Dez | EBIT-Wirkung | Annahmen |
|---|---|---|
| A Ursache behoben Mitte Oktober | rund -324 | Sep voll, Okt halb; KT-900 CHF 60k |
| B Weiter wie bisher | rund -908 | Qualitätskosten 398 Jun bis Aug, skaliert mit Budget-Materialaufwand (Q4 saisonal mehr als doppelt so viel Volumen) |
| C wie B, plus Auslistung Dunkel bei FrischMarkt ab Oktober | rund -1'714 | zusätzlich Deckungsbeitrag FrischMarkt Dunkel Okt bis Dez 2025: 806 (Netto 1'563 minus Material 757) |

Ohne Skalierung (gleich hohe Kosten wie im Sommer) wären es in B rund -531. Die Szenarien sind Rechnungen auf Annahmen, keine Prognose.

**Einordnung:** Die Einsparung von CHF 38'000 bei der Maschine steht gegen Qualitätskosten von rund 100 bis 130 TCHF pro Monat im Sommer.

## 5. Was tun wir jetzt? (Vorschläge)

1. **Sofort (diese Woche):** Temperierkurven und Ausschuss auf L2 prüfen lassen (QS und Produktion). Bestätigt sich der Zusammenhang: Entscheid über Ersatz durch KT-900 (Offerte CHF 60k, Lieferfrist klären).
2. **Kunde FrischMarkt:** Gespräch auf Stufe GL mit Qualitätsmassnahmenplan, verstärkte Ausgangskontrolle Dunkel, bis die Ursache behoben ist.
3. **Reporting:** Ausschussreport im ERP-Modul korrigieren; Material Ist gegenüber Standard und Retourenquote pro Linie monatlich (nicht YTD) ins Monatsreporting.
4. **Governance:** Ersatz von qualitätskritischen Anlagen nicht durch Einkauf allein, sondern mit Produktion und QS freigeben.

## 6. Skeptiker-Check

**Zwei Zahlen zum Nachrechnen in Excel**
1. Überstunden Jun bis Aug über Budget: ER-Export, Konto 5050, Zeilen 2026-06 bis 2026-08: (53'533 + 67'123 + 50'920) minus (4'752 + 4'193 + 4'472) = 171'576 minus 13'417 = 158'159.
2. Retourenquote Dunkel Juli: Umsatzdatei, Filter Periode 2026-07 und SKU TD70, TD85, TDO: Summe Retouren 41.6 TCHF geteilt durch Summe Bruttoumsatz 781.4 TCHF = 5.3 %.

**Aussage zum Widerlegen:** «Die Temperiermaschine ist die Ursache.» Gegenargumente aus den Daten:
* Überstunden lagen schon Feb bis Apr über Budget (14.0 / 23.0 / 15.6), also vor dem Einbau. Teile davon erklärt das vorgezogene Ostergeschäft (Feb/Mär Menge über Budget), April nicht.
* Die neue Rezeptur Dunkel 85 % (Launch 04.05.) fällt zeitlich ebenfalls zusammen. TD85 hatte im Mai die höchsten Retouren (20.4).
* Der Material-Mehrverbrauch ist eine Restgrösse und enthält auch Lager- und Abgrenzungseffekte (F7 offen).
Fazit: Linie 2 als Ort ist gut belegt. Ob die Maschine, die Rezeptur oder beides die Ursache ist, entscheiden erst die Werksdaten.

## 7. Neue Fragen an die CFO (wenn der Chat wieder antwortet)

Format: «Was ich wissen will» und «Was ich in den Daten gesehen habe», je eine Frage.
* **F15 Rezeptur vs. Maschine:** Wurde die neue Rezeptur Dunkel 85 % vor oder nach dem 06.04. erstmals auf L2 produziert, und sind TD70 und TDO von der Rezeptur betroffen? Gesehen: Retouren steigen bei allen drei Dunkel-Produkten, nicht nur TD85.
* **F16 Lieferfrist KT-900:** Ist die Offerte für die KT-900 noch gültig, und wie lange ist die Lieferfrist? Gesehen: Qualitätskosten rund 100 bis 130 TCHF pro Monat, Szenario A hängt vom Zeitpunkt ab.
* **F17 FrischMarkt:** Was war das Ergebnis des Gesprächs vom 21.07.? Gesehen: Dunkel-Menge FrischMarkt Jul/Aug 8.5 / 8.2 t statt 12.2 / 13.0 t; Deckungsbeitrag Dunkel Okt bis Dez 2025 bei FrischMarkt 806 TCHF.
* Weiterhin offen: F2 Ausschuss L2, F3 Überstunden nach Linie, F4 Temperaturen.
