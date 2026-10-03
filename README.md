# Sennhof Schokolade: Analyse für die CFO

Gruppenarbeit zur Fallstudie Sennhof. Die CFO (Nadia Rossi) muss dem Verwaltungsrat erklären, warum Sennhof seit Juni 2026 rund CHF 150 bis 190k pro Monat unter Budget liegt, ob es weitergeht und was zu tun ist. Alle Beträge in TCHF, Abweichung = Ist gegenüber Budget V3.

Arbeitsregeln für die Analyse (belegt gegen vermutet, Rohdaten nie verändern, jede Zahl aus einem Skript) stehen in [CLAUDE.md](CLAUDE.md).

## Ordnerstruktur

| Pfad | Inhalt |
|---|---|
| `CLAUDE.md` | Auftrag, Arbeitsregeln, Datenlandkarte, Hypothese |
| `Sennhof Analyse Stand.md` | Aktueller Stand der Analyse mit Belegen |
| `Sennhof Fragenkatalog CFO.md` | Fragen an die CFO |
| `CFO_Antworten.md` | Antworten der CFO |
| `analyse/` | Python-Skripte (`bruecke.py`, `grafiken.py`); jede Zahl entsteht hier |
| `grafiken/` | Erzeugte Charts (PNG) |
| `ergebnisse/` | Zahlen als CSV, `belegliste.md`, `rueckfragen_cfo.md` (geplant) |
| `praesentation/` | 4-Minuten-Präsentation, max. 6 Folien (geplant) |

## Nicht im Repo (Kursdaten, Copyright)

Diese Dateien liegen nur lokal und stehen in `.gitignore`:

* `Paket_1_Finanzen.zip` und der entpackte Ordner `Paket_1_Finanzen/`
* `Paket_2_Werk/`
* `Sennhof Auftrag Teil 1*`

Die Daten beschafft sich jede Person selbst aus dem Kurs und entpackt sie im Projektordner.

## Skripte ausführen

Die Skripte lesen relative Pfade und laufen im entpackten Datenordner:

```bash
cd Paket_1_Finanzen
python ../analyse/bruecke.py
```

Benötigt Python mit `pandas` (und `matplotlib` für `grafiken.py`).

## Arbeitsweise

1. **Ein Branch pro Person**, benannt nach der Person, z. B. `rino`, `anna`. Nie direkt auf `main` arbeiten.
2. **Änderungen nur per Pull Request auf `main`.** Mindestens eine andere Person schaut drauf, bevor gemerged wird.
3. Vor dem Arbeiten `main` holen und in den eigenen Branch übernehmen: `git pull origin main`.
4. Kleine, thematisch klare Commits mit verständlicher Nachricht.
5. Zahlen gehören in Skripte unter `analyse/`, nicht von Hand in Texte. Jede Zahl im Text braucht eine Quelle (Datei, Konto, Periode, Wert).
6. Keine Kursdaten committen. Vor jedem Commit `git status` prüfen.
