# Path-Viewer

Der Path-Viewer ist zum Visualisieren einer Strecke. Der Graph entsteht durch Verbinden einer geordneten Punktmenge. Momentan wird eine CSV-Datei in eine animierte GIF-Datei umgewandelt.

## Vorbereitung

Zum Konvertieren wird *gnuplot* verwendet. Dieses Programm kann unter anderem Funktionen oder Datafiles plotten und unterstützt einfache "Programmierung" sowie 3D-Ansichten.

Unter **Linux** lässt sich *gnuplot* mit dem Befehl ``sudo apt-get install gnuplot`` installieren. 

Der Downloadlink für **Windows** findet sich auf der [offiziellen sourceforge-Seite](http://sourceforge.net/projects/gnuplot/files/gnuplot/). Die neusten Versionen sind noch nicht für Windows kompiliert. :P

## Struktur der Input-Datei

Der Viewer findet sich [in diesem Repository](../viewer/). Die zu kompilierenden Daten in der CSV-Datei. Jeder Datensatz ist in einer Zeile: X-Y-Z-Werte, welche Punkte im geodätischen Koordinatensystem angeben, jeweils durch ein Komma getrennt. **Die Datei muss** ``path.csv`` **heißen!** Wie zum Beispiel im folgenden Beispiel.

```
0;0;0
6.12323399574e-17;0.0;1.0
1.22416393426e-16;2.43126671095e-18;2.0
1.83452944217e-16;7.3240086955e-18;3.0
0.0150750099354;0.000696442934122;3.99988612304
0.0431386039101;0.000765932433057;4.99949226041
0.0686875022713;0.000400095172706;5.99916576708
0.118577732094;-0.000841188844022;6.99791970284
0.145769637833;-0.00100363132129;7.99754992141
0.217409806669;-0.00105053822041;8.99498046235

...
```

Diese Werte (auch mit dem Exponenten wie z.B. ``e-17``) sind Float-Werte, die Python nach der Konvertierung in einen String zurückgibt.

## Konvertierung

Zum Konvertieren startet man unter Linux den Terminal (Konsole). Unter Windows funktioniert es ähnlich. Nach dem Navigieren in das Repository-Verzeichnis ``lk-info-quadcopter/viewer/`` führt man in dieser Konsole den Befehl ``gnuplot "pviewer.gnuplot"`` aus. Nun sollte *End of animation sequence* in der Konsole stehen und in dem gleichen Ordner eine ``outp.gif`` befinden.

Die animierte GIF-Datei kann mit jedem beliebigen, guten Bildbetrachter angeschaut werden. 

## Pläne

Nun, ehrlich gesagt ist eine Ausgabe in eine GIF-Datei keine endgültige Lösung. Zwar lässt sich diese Datei gut in HTML-Dateien (auch Markdown) als Live-Preview  eingebaut werden, aber es ist nicht möglich den Graphen beliebig zu drehen. Auch eine Datei erstellen zu müssen ist nicht elegant, im Vergleich zu einem Programm, welches die CSV-Datei beim Start liest und ein freies Bewegen anhand der Pfeiltasten ermöglicht.