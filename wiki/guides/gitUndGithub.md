# Git und Github

Dieses Dokument fasst die am 2013-12-20 präsentierten Grundlagen für die Benutzung von Git und Github zusammen.

## Konzept hinter Git und Github


Git ist ein sogenanntes [Versionsverwaltungssystem](de.wikipedia.org/wiki/Versionsverwaltungssystem), d. h., es dient dazu, auf dem Computer schrittweise Änderungen an einem Projekt zu erfassen. Git wird mit der Konsole bedient und ist Open Source. Es ist für Linux, Mac OS und Windows frei erhätlich.

Github ist ein Online-Portal, das auf Git aufbaut und die Kollaboration über Git ermöglicht. Github bietet an, Git-Projekte auf einem Server aufzusetzen. Mehrere Mitarbeiter können dann davon lokale Kopien erstellen, dann an diesen lokalen Kopien lokal (d. h. auch ohne Internetanschluss) herumarbeiten, entwickeln, programmieren etc., bis sie sich entscheiden, die gemachten Änderungen wieder in das gemeinsame Repository bei Github hochzuladen, sodass diese Änderungen allen anderen Mitarbeitern zugänglich sind.


## Git-Grundlagen

Für ein *Projekt* stellt ein Ordner stets die Wurzel dar. Solch ein Ordner wird auch *Repository* genannt. Den gesamten Arbeitskreislauf beginnt man für gewöhnlich, indem man von einem bereits existierenden, öffentlichen Repository eine lokale Kopie erstellt; dieser Vorgang nennt sich *Klonen*. Der dazu genutzte Befehl ist

```bash
git clone https://github.com/beispieluser/beispielRepository.git
```

Führt man dies in einem Ordner "Dokumente" aus, so erstellt Git das Repository im Ordner "Dokumente/beispielRepository". Für alle weiteren Arbeiten mit Git sollte man nun in diesen Ordner wechseln, üblicherweise mit `cd beispielRepository`.

Im Repository befinden sich zum einen alle Projektdateien (der gesamte Projektbaum), zum anderen im .git-Verzeichnis die Datenbank, die Git führt, um auf Anfrage alle älteren Versionen zur Verfügung zu stellen. Git selbst arbeitet zunächst bloß lokal auf dem Rechner. Um das lokale Repository zu aktualisieren, ohne zu klonen (Klonen ist nur beim allerersten Mal zu verwenden), verwendet man

```
git pull
```

Nun beginnt die Arbeit selbst: Dazu bearbeitet man einfach wie gewöhnlich die im Repository befindlichen Projektdateien. Z. b. implementiert man nach Herzenslust mit dem Lieblings-Texteditor ein neues Feature oder fixt einen Bug. Wenn man dabei neue Dateien erstellt, so muss man dies Git über den Befehl

```bash
git add beispielhafteNeueDatei.pas
```

mitteilen. Man kan dem add-Befehl auch ganze Verzeichnisse, darunter auch . als Parameter übergeben. Will man eine Datei vom Projekt entfernen, so nutzt man dafür ganz ähnlich `git rm beispielDatei.pas` und löscht die Datei danach manuell. So weiß Git stets, welche Dateien es speichern soll, wenn man einen *Commit* erstellt:

Ist ein Feature erfolgreich implementiert -- d. h. insbesondere auch, dass nach Testen keine erkennbaren Fehler mehr auftreten -- oder ein Bug gefixt, so sagt man Git, dass es eine Art Momentaunahme des Repositorys als einen sogenannten *Commit* speichern soll. Zusätzlich zu einer solchen Momentaufnahme (dem Commit) wird der Name desjenigen, der diesen Commit erstellt hat, sowie eine kurze Nachricht, die den Commit beschreibt, gespeichert. Der Befehl dazu lautet

```bash
git commit -am "Bug Nr. 314 gefixt."
```

Man sollte dabei darauf achten, dass ein Commit stets für genau eine in sich vollständige, logische Änderung am Projekt stehen sollte, also zum Beispiel eine neue Funktionalität oder ein Bugfix. Niemals sollte ein Commit erstellt werden, wenn der Code bekanntermaßen Fehler enthält. Würde dies geschehen, so müssten Andere mit einer fehlerhaften Version weiterarbeiten. Es sollte auch nicht nach jeder einzelnen Zeile Code (und auch nicht nach jedem Dutzend!) ein Commit erstellt werden. Außerdem sollten nicht mehrere thematisch unterschiedliche Änderungen in einem Commit vollzogen werden. Wie man den letzten Punkt erfüllt, wenn man gerade an mehreren verschiedenen Dingen arbeitet, wird weiter unten in *Git Branching* erklärt.

Nach einigen solcher Commits hat man eine Art lineare Historie erstellt:

```
C1 --> C2 --> C3
```

Ist man nun bereit, diese Änderungen mit seinen Mitarbeitern zu teilen, so sollte man schließlich

```bash
git push origin master
```

verwenden. Dies sorgt dafür, dass Git die gemachten Änderungen auf den bisher unwissenden Server hochlädt, von dem geklont wurde, sodass alle Anderen die Änderungen ebenfalls sehen können. Dabei können nun aber Konflikte auftreten, wenn in der Zwischenzeit andere auch Änderungen *gepusht* haben. Um solche Konflikte zu lösen und generell auf eine besser organisierte Weise am Code zu arbeiten, sodass nicht alles in einem großen Chaos endet, wurde das Konzept des *Branching* eingeührt.

### Zusammenfassung

0. Ein einziges Mal zu Beginn aller Arbeit: `git clone https://github.com/beispieluser/beispielRepository.git`. Alles Weitere findet im erstellten Repository statt. Normalerweise werden mit `git pull` die neusten Änderungen vom Server heruntergeladen.
1. Dann wird ganz normalen Projekt gearbeitet. Neue Dateien werden mit `git add datei.txt` hinzugefügt und mit `git rm datei.txt` nebst manuellem Löschen entfernt.
2. Ist eine in sich vollständige, logische Änderung vollzogen, so wird ein Commit erstellt mit `git commit -am "sinnvolle Beschreibung"`.
3. Soll die Arbeit mit den Anderen geteilt werden, so schreibt man einfach `git push origin master`.



## Git Branching

Bisher verlief die Commit-Historie stets linear. Nun werden sogenannte *Branches*, zu deutsch Zweige, die Sache deutlich interessanter machen. Branches werden unter anderem verwendet, um an einzelnen, thematisch voneinander verschiedenen Änderungen seperat voneinander zu arbeiten. Dazu erstellt man einen solchen Themen-Branch und erstellt an ihm einige Commits. Ist die Arbeit getan, so führt man den neu entstandenen Themen-Zweig und den Hauptzweig wieder zusammen, auch *merging* genannt, um ein Endresultat zu erhalten.

Einen Branch kennen wir schon, nämlich den master-branch. Auf dem haben wir bis jetzt stets gearbeitet. Ein Branch besteht an sich aus nichts mehr als einem Zeiger auf den aktuellsten Commit auf dem Branch, etwa so

```
            master
              |
              V
C1 --> C2 --> C3
```

Der Zeiger wurde bei neuen Commits stets weitergerückt, da wir uns stets auf dem master-Branch befanden. Um einen neuen Branch zu erstellen, muss Git zunächst nichts weiter tun, als einen neuen Zeiger auf den aktuellen Commit zu erstellen. Das funktioniert mit 

```
git branch bugfix40
```

Das Ergebnis ist dann

```
       master    bugfix40
             \  /
              \/
C1 --> C2 --> C3
```

Um den bugfix40-Branch nun den aktiven Branch zu machen, an dem man arbeitet, verwendet man

```
git checkout bugfix40
```

Das aktualisiert auch das gesammte Projektverzeichnis so, dass alle Dateien genau so aussehen, wie auf dem bugfix40-Branch. Da der momentan aber noch auf den selben Commit wie der master-Branch zeigt, ändert sich erstmal nicht viel.

Nun wird am Bugfix Nummer 40 gearbeitet und ein ganz normaler Commit erstellt, der das Problem behebt, z. B. durch `git commit -am "Bug Nummer 40 gefixt."`. Das erzeugt folgendes Resultat:

```
       master    bugfix40
             \       |
              \      |
C1 --> C2 --> C3 --> C4
```

Nehmen wir an, Mitarbeiter X hat in der Zwischenzeit auch einen Bug gefixt und seine Änderungen bereits in den master-Branch auf dem Server geladen. Um von diesen Änderungen zu erfahren, wechseln wir zunächst mit `git checkout master` auf den master-Branch zurück unf führen dann `git pull` aus. Danach könnte unser lokales Repository wie folgt aussehen.

```
                 bugfix40
                     |
                     |
C1 --> C2 --> C3 --> C4
               \
                +--> C5
                     |
                     |
                  master
```

Der master-Branch hat sich also wegen des C5-Commits von Mitarbeiter X von unserer bugfix40-Historie abgezweigt. Der checkout-befehl hat auch alle Dateien in unserem Repository geändert: Alle Änderungen, die in C4 gemacht wurden, sind verschwunden und dafür können wir nun die Änderungen, die Mitarbeiter X gemacht hat, bewundern. Unser Bugfix ist aber nicht verloren : Jetzt wollen wir beide wieder zusammenführen, genauer gesagt, wollen wir den bugfix40-Branch in den master-Branch *mergen*. Dazu führen wir 

```
git merge bugfix40 -m "Beschreibung des Merges"
```

aus. Gibt es keine Konflikte, so erstellt Git automatisch einen neuen Commit, der das "Kind" von C4 und C5 ist, mit der angegebenen Beschreibung, in etwa wie folgt.

```
                 bugfix40
                     |
                     |
C1 --> C2 --> C3 --> C4 ---+
               \            \
                +--> C5 --> C6
                            |
                            |
                         master
```

Eventuell tritt jedoch ein Konflikt auf. Darüber informiert Git mit einer Fehlermeldung beim merge-Befehl. Es wird in diesem Fall kein neuer Commit erstellt, jedoch werden alle Dateien im Repository so gut es geht geändert. An den Konfliktstellen werden wird folgendes in die Dateien eingefügt.

```
<<<<<<< HEAD
Code, der vom Mitarbeiter X auf dem master-Branch geschrieben wurde
=======
Code, der für den Bugfix geschrieben wurde
>>>>>>> bugfix40
```

Man sollte diese Stellen nun abgehen und -- bei Unsicherheit auch gerne erst nach Absprache mit dem Rest der Entwickler -- den gewünschten Code stehen lassen. Um den Merge-Vorgang dann abzuschließen, wird ein ganz normaler Commit ausgeführt mit `git commit -am "Beschreibung des Merges"`, was in einem Commit C6 wie in der obigen Abbildung resultiert.

Zu guter Letzt sollte noch der nun überflüssig gewordene Zeiger bugfix40 entfernt werden, das geschieht mit

```
git branch -d bugfix40
```


Die folgenden beiden Punkte sollen noch am Dienstag nach den Ferien besprochen werden.


## Die Github-Oberfläche


## Unser Workflow