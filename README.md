# Challenge: Make the pipeline green

**Dauer:** max. 20 Minuten  
**Werkzeug:** nur der Texteditor im Browser (GitHub Web-Editor). Es muss nichts lokal installiert werden.

## Szenario

Das Monitoring-Team will Zertifikate nach ihrer Restlaufzeit einstufen. Die Funktion dafür ist noch nicht
geschrieben, und die automatische Prüfung (GitHub Action) ist kaputt. Deine Aufgabe ist, beides zu reparieren,
sodass die Action **grün** wird.

## Dateien

| Datei | Inhalt |
| --- | --- |
| [python/cert_status.py](python/cert_status.py) | Funktion, die du implementierst |
| [python/test_cert_status.py](python/test_cert_status.py) | Vorgegebene Tests (pytest) |
| [.github/workflows/challenge-python.yml](.github/workflows/challenge-python.yml) | GitHub Action, die die Tests ausführt |
| [HINTS.md](HINTS.md) | Hilfestellung, falls du nicht weiterkommst |

## So arbeitest du

1. Öffne eine Datei in GitHub und klicke auf das Stift-Symbol (Edit).
2. Klicke auf **Commit changes...** und wähle **Create a new branch for this commit**.
   Der Branchname ist beliebig, **aber nicht `master`**. Bei den weiteren Commits bleibst du auf diesem Branch.
3. Jeder Commit startet die Action automatisch. Das Ergebnis siehst du im Tab **Actions**.
   Ein Klick auf den Lauf und dann auf den Job zeigt das Log mit der Fehlermeldung.

## Aufgaben

1. **Workflow reparieren**  
   Im Workflow sind **2 Fehler**. Finde sie mithilfe der Logs und behebe sie.
   Mehr als diese beiden Fehler gibt es nicht.
2. **Funktion implementieren**  
   Die Funktion ist als Stub vorhanden und die Tests sind vorgegeben. Implementiere sie so, dass alle Tests grün sind.

   | Restlaufzeit in Tagen | Ergebnis |
   | --- | --- |
   | keine Angabe (`None`) | `UNKNOWN` |
   | kleiner als 0 | `EXPIRED` |
   | 0 bis 7 | `CRIT` |
   | 8 bis 30 | `WARN` |
   | mehr als 30 | `OK` |
   
## Regeln

- Die Tests und der Workflow dürfen angepasst werden, wenn es nötig ist. Die Tests dürfen aber nicht
  abgeschwächt werden, nur damit sie grün werden.
- Internet und Dokumentation sind erlaubt. KI-Assistenten nur nach Absprache.
- Fragen an den Interviewer sind erlaubt und erwünscht.
- Nicht jeder Commit muss grün sein. Wir schauen vor allem darauf, **wie** du vorgehst.
- Wenn du nicht weiterkommst, hilft dir [HINTS.md](HINTS.md).

## Dokumentation

| Thema | Link |
| --- | --- |
| Tests ausführen und Ausgabe lesen | [pytest usage](https://docs.pytest.org/en/stable/how-to/usage.html) |
| Abhängigkeiten aus Datei installieren | [pip requirements files](https://pip.pypa.io/en/stable/user_guide/#requirements-files) |
| Verzweigungen in Python | [Python `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements) |