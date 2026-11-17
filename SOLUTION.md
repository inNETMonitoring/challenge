# Lösung: Schritt für Schritt

> **Nur für Interviewer.** Dieser Ordner (`_solution`) wird vor der Freigabe an Kandidaten entfernt.

## 1. Workflow reparieren

Datei: [.github/workflows/challenge-python.yml](../.github/workflows/challenge-python.yml)

Die Fehler erscheinen nacheinander im Log. Nach dem Fix von Fehler 1 tritt Fehler 2 auf.

### Schritt 1.1: Fehler im Schritt `Install dependencies`

1. Actions-Tab öffnen, fehlgeschlagenen Lauf und Job anklicken.
2. Im Log steht:
   `ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'`
3. Ursache: Der Schritt läuft im Repo-Root, die Datei liegt aber in `python/`.
4. Fix:

   ```yaml
   run: pip install -r python/requirements.txt
   ```

5. Committen und das Ergebnis in Actions abwarten.

### Schritt 1.2: Fehler im Schritt `Run tests`

1. Neuer Lauf, der Schritt `Install dependencies` ist jetzt grün. Im Log von `Run tests` steht:
   `ERROR: file or directory not found: pyhton`
2. Ursache: Tippfehler im Ordnernamen.
3. Fix:

   ```yaml
   run: pytest python
   ```

4. Committen. Der Workflow läuft jetzt bis zu den Tests. Diese sind **rot**, bis die Funktion implementiert ist. Das ist so gewollt.

## 2. Funktion implementieren

Datei: [python/cert_status.py](../python/cert_status.py)

### Schritt 2.1: Log lesen

Im Log schlagen alle 9 Tests mit `NotImplementedError: TODO: implementieren` fehl.

### Schritt 2.2: Funktion schreiben

Ersetze `raise NotImplementedError(...)` durch:

```python
if days_left is None:
    return "UNKNOWN"
if days_left < 0:
    return "EXPIRED"
if days_left <= 7:
    return "CRIT"
if days_left <= 30:
    return "WARN"
return "OK"
```

### Schritt 2.3: Committen und prüfen

Nach dem Commit sind alle 9 Tests und damit die Action **grün**.

Typische Stolpersteine:

- **Grenzwerte:** 7 gehört zu `CRIT`, 30 gehört zu `WARN`. Bei `<` statt `<=` schlagen die Tests fehl.
- **Reihenfolge:** `None` muss zuerst geprüft werden, sonst gibt `None < 0` einen `TypeError`.
- **`0 Tage`:** ist `CRIT` und nicht `EXPIRED`.
