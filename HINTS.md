# Hinweise

Versuche es zuerst allein. Öffne pro Aufgabe nur so viele Hinweise, wie du brauchst (von oben nach unten).
Du kannst dem Interviewer jederzeit Fragen stellen.

## Aufgabe 1: Workflow reparieren

1. Öffne den Tab **Actions**, klicke auf den fehlgeschlagenen Lauf und dann auf den Job.
2. Klappe den roten Schritt auf und lies die Fehlermeldung. Sie sagt, was fehlt.
3. Der Workflow läuft im Hauptordner des Repos. Wo liegen die Dateien, die der Schritt braucht?
4. Vergleiche Dateinamen und Ordner im Befehl Buchstabe für Buchstabe mit der Ordnerstruktur.
5. Behebe pro Commit **einen** Fehler und warte auf das Ergebnis. Nach dem ersten Fix kommt der zweite Fehler zum Vorschein.

## Aufgabe 2: Funktion implementieren

1. Lies die Tests in [python/test_cert_status.py](python/test_cert_status.py). Sie zeigen die erwarteten Werte inklusive Grenzfällen.
2. Die Tabelle in der [README](README.md) lässt sich direkt in `if`-Abfragen übersetzen.
3. Prüfe zuerst den Sonderfall `None`. Mit `None` kann man nicht rechnen oder vergleichen.
4. Achte auf die Grenzen: 7 gehört noch zu `CRIT`, 30 noch zu `WARN`. Überlege, ob `<` oder `<=` passt.
5. Gehe die Fälle von klein nach gross durch: `EXPIRED`, `CRIT`, `WARN`, sonst `OK`.

## Aufgabe 3: Antwort

Überlege dir diese vier Punkte und fasse sie in 2 bis 3 Sätzen zusammen:

- **Ausführen:** Wo läuft der Check?
- **Schedulen:** Wie wird er täglich gestartet?
- **Alarmieren:** Wie erfährt das Team von `CRIT` und `EXPIRED`?
- **Zugangsdaten:** Wo werden Passwörter und Tokens abgelegt (nicht im Repo)?

## Bonus-Test

Überlege dir, was in der Praxis schiefgehen kann, zum Beispiel negative Werte, Text statt Zahl oder ein Wert genau auf der Grenze.
Schreibe dafür einen weiteren Eintrag in `test_classify_cert` oder einen neuen Test.
