# Hover-Mode

von Sebastian

Dieses Dokument beschreibt die theoretische Umsetzung eines Hover-Modes und die Umsetzung zwischen Drohne(-nbewegungsrichtung) und Welt(-bewegungsrichtung).

## Allgemein

### Definition

Der Hover-Mode ist ein Bewegungsmodus, bei dem man sich konstant auf einem Punkt stehen bleibt und sozusagen schwebt. Des weiteren kann man sich, ausgehend von diesem Schwebezustand in verschiedene Richtungen mit veschiedenen, festgelegten Geschwindigkeiten bewegen.

### Startbedingungen

Die Drohne besitzt Beschleunigngssensoren, die ihre Angaben relat zur Neigung der Drohne angeben. Ist die Drohne also  gedreht, geben die Beschleunigungssensoren  die Werte "verdreht" wieder. Gegeben ist also von der **Drohne aus Neigung** und die **Beschleunigung**. Desweiteren nehme ich auch die **"Momentangeschwindigkeit" der Drohne** als Vorrausetung an, siehe unten. 

Die **Zielgeschwindigkeit der Drohne** ist die anzusteuernde Richtgeschwindigkeit absolut im Weltkoordinatensystem. Um diesen (möglichst schnell) zu erreichen, muss mit einer **Gegenbewegung** ausgeglichen werden.

![Startbedingungen](pict_hover/Startbedingungen.png)

### Funktionsweise

Wir nehmen die aktuelle Geschwindigkeit der Drohne und transformieren sie in das Weltkoordinatensystem (geogätisches Koordinatensystem). Nun haben wir den Geschwindigkeitsvektor der Drohne v<sub>Drohne</sub>, welcher in der unternstehenden Abbildung eingetragen ist.

Zusammen mit dem Zielgeschwindigkeitsvektor v<sub>Ziel</sub> wird im zweiten Schritt die Ausgleichbewegung v<sub>Gegen</sub> bestimmt. 

v<sub>Gegen</sub> im geodätischen Koordinatensystem wieder ins drohnenfeste Koordinatensystem transformiert mit den Motoren (*roll*, *pitch*, *thrust*; *yaw* nicht benötigt) umgesezt.

![Koordinatensystem](pict_hover/3D-Koordinatensystem.png)

## 1. Schritt: Drohne zur Welt

Die Drohne ist ein sich frei im Raum bewegendes Objekt, welches sich auch gekippt im Raum (im folgenden "*geodatisches Koordinatensystem*" genannt) befinden kann. Alle Angaben, die wir zur Drohne über Sensoren erhalten sind relativ zur Drohnenposition und -neigung (im "*drohnenfesten Koordinatensystem*"). Möchten wir zum Beispiel nun wissen, in welche Richtung die Drohne sich gerade bewegt, müssen wir den Geschwindigkeitsvektor (zusammengesetzt aus v<sub>Drohne;x</sub>, v<sub>Drohne;y</sub> und v<sub>Drohne;z</sub>) vom drohnenfesten Koordinatensystem in das geodätische Koordinatensystem transformieren.

Dabei drehen wir nicht den Vektor, sondern "nur" das Koordinatensystem. 

###  Die Koordinatensysteme

Das ***geodätische Koordinatensystem*** ist, wie der Name verrät, erdfest. Dabei wird normalerweise die **x-Richtung nach Norden** angenommen. Nach der Rechte-Hand-Regel ist dann die **y-Richtung nach Osten** und die **z-Richtung ZUM BODEN**. 

Das ***drohnenfeste Koordinatensystem*** ist an der Drohne  festgemacht und der Ursprung befindet sich im Schwerpunkt des Koordinatensystems. die **x-Achse zeigt nach vorne**, die **y-Achse zeigt nach rechts** und die **z-Achse nach unten**. Wenn die Drohne beispielsweise die "Nase" hochnimmt, bewegt sich also das drohnenfeste Koordinatensystem mit und bei jeder Bewegung wird das drohnenfeste Koordinatensystem mitbewegt. 

### Theorie

Nach den Eulerschen Winkeln ergeben sich andere Transformationen, wenn man andere Winkel zuerst dreht. Die Drohne verwendet ein in der Fahrzeugtechnik gebräuchliches System des [" z, y', x'' "-Standards](http://de.wikipedia.org/wiki/Eulersche_Winkel#.E2.80.9Ez.2C_y.27.2C_x.27.27-Konvention.E2.80.9C_in_der_Fahrzeugtechnik). Sie besteht aus einer Neigung um *yaw*, *pitch *und *roll* in dieser Reihenfolge.

### Mathematik

Die Matrizenmultiplikation ist eine nicht kommutative Gruppe. 

Drehen wir vom geodätischen Koordinatensystem in das drohnenfeste Koordinatensystem müssen wir folglich zuerst um die z-Achse (z; yaw), dann um die neue y-Achse (y'; pitch) und dann um die neue-neue x-Achse (x''; roll) drehen. Dieser Vorgang ist im dritten Schritt genauer erklärt. Ich setze die dort erarbeitete Matrix vorraus, nimm sie erst einmal als korrekt hin.

![WeltZuDrohneMatrix](pict_hover/WeltZuDrohneMatrix.png)

Die Transformation vom drohnenfesten Koordinatensystem ins geodätische Koordinatensystem ist die entgegengesetzte Transformation zur Rücktransformation. Wir drehen also nicht Gier ~ Nick ~ Roll, sondern -Roll ~ -Nick ~ -Gier. Die zuletzt durchgeführte Transformation machen wir also mit dem negativen Winkel zuerst rückgängig. 

In der Praxis jedoch ist es viel einfacher! Besitzt man eine Transformationsmatrix in eine Richtung, ist die Transformationsmartix in die anderere Richtung die transpornierte Matrix. Es gilt:

![DrohneZuWelt](pict_hover/DrohneZuWelt.png)

Multipliziert man diese riesige Matrix mit einem Vektor im drohnenfesten Koordinatensystem erhält man diesen Vektor im geodätischen Koordinatensystem:

![DrohneZuWelt2](pict_hover/DrohneZuWelt2.png)

## 2. Schritt: Berechnung der neuen Ausgleichbewegung

Nun haben wir also unsere aktuelle Bewegung der Drohne UND unsere Zielbewegung im Weltkoordinatensystem. Die Ausgleichbewegung muss folglich (wie bei einem Kräfteparallelogramm zusammen mit der aktuellen Bewegung die Zielbewegung sein.

![Drohne-Ziel-Gegen-Paralellogramm](pict_hover/Drohne-Ziel-Gegen-Paralellogramm.png)

### Berechnung

Daraus ergibt sich folgendes Gleichungssystem:

![Drohne-Ziel-Gegen-Gleichung](pict_hover/Drohne-Ziel-Gegen-Gleichung.png)

Die Gegenbewegung ist gleich der Zielbewegung minus die aktuelle Bewegung.

## 3. Schritt: Umsetzung der Gegenbewegung

Die Gegenbewegung v<sub>G</sub> ist im Weltkoordinatensystem. Um sie sinnoll verwenden zu können, transformieren wir diesen Vektor ins Drohnenkoordinatensystem zurück, um ihn dann in seine Bestandteile aufzuteilen.

### Rücktransformation

Die Rücktransformation ist ähnlich zur Transformation vom drohnenfesten Koordinatensystem ins geodätische Koordinatensystem. Die Transformation M<sub>dg</sub> vom geodätischen ins drohnenfesten Koordinatensystem ist über die drei Eulerwinkel definiert:

- psi - Gierwinkel (Auslenkung aus der Nordrichtung; Drehung um z-Achse)
- theta - Nickwinkel (Anhebung der "Nase" über die Erdhorizontale)
- phi - Rollwinkel (Neigung der rechten Hälte nach unten)

![Lagewinkel-Drehung-WeltZuDrohne](pict_hover/Lagewinkel-Drehung-WeltZuDrohne.png)

Das geodätische Koordinatensystem ist das rote Koordinatensystem, wobei x<sub>g</sub> Richtung Norden, y<sub>g</sub> Richtung Osten und z<sub>g</sub> Richtung Erdmittelpunkt ausgerichtet ist. Um ins drohnenfeste Koordinatensystem zu gelagen, drehen wir zuerst um den Gierwinkel (die roten Winkel; um die z<sub>g</sub>-Achse mit psi); nun um den Nickwinkel (grün; um die k<sub>2</sub>-Achse mit dem Winkel theta); dann um den Rollwinkel (blau; um die x<sub>f</sub>-Achse mit dem Winkel phi).

![WeltZuDrohne](pict_hover/WeltZuDrohne.png)

Multiplizieren wir die folgende Matrix mit einem Vektor aus dem geodätischen Koordinatensystem, erhalten wir diesen Vektor im drohnenfesten Koordinatensystem:

![WeltZuDrohneVektor](pict_hover/WeltZuDrohneVektor.png)

### Umsetzug in Motoren

Nun teilen wir den Vektor in die Bestandteile auf. v<sub>d;Gegen;x</sub> übersetzen wir mit zusätzlichem *roll* - wir multipizieren v<sub>d;Gegen;x</sub> mit einem Balancefaktor und addiren es zu unserem bisherigem *roll*. Gleiches Prinzip führen wir mit v<sub>d;Gegen;y</sub> und *pitch* durch, sowie mit v<sub>d;Gegen;z</sub> und *thrust*.

Als Balancefaktor haben wir bisher **noch keine für v<sub>G;x</sub> und v<sub>G;y</sub>** ausmachen können. Misst man alle 10ms, bietet sich allerdings **2500 für <sub>G;z</sub>** an.