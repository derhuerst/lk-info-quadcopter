# Hover-Mode

Dieses Dokument beschreibt die theoretische Umsetzung eines Hover-Modes und die Umsetzung zwischen Drohne(-nbewegungsrichtung) und Welt(-bewegungsrichtung).

## Allgemein

### Definition

Der Hover-Mode ist ein Bewegungsmodus, bei dem man sich konstant auf einem Punkt stehen bleibt und sozusagen schwebt. Des weiteren kann man sich, ausgehend von diesem Schwebezustand in verschiedene Richtungen mit veschiedenen, festgelegten Geschwindigkeiten bewegen.

### Startbedingungen

Die Drohne besitzt Beschleunigngssensoren, die ihre Angaben relat zur Neigung der Drohne angeben. Ist die Drohne also  gedreht, geben die Beschleunigungssensoren  die Werte "verdreht" wieder. Gegeben ist also von der **Drohne aus Neigung** und die **Beschleunigung**. Desweiteren nehme ich auch die **"Momentangeschwindigkeit" der Drohne** als Vorrausetung an, siehe unten. 

Die **Zielgeschwindigkeit der Drohne** ist die anzusteuernde Richtgeschwindigkeit absolut im Weltkoordinatensystem. Um diesen (möglichst schnell) zu erreichen, muss mit einer **Gegenbewegung** ausgeglichen werden.

![Startbedingungen](pict_hover/Startbedingungen.png)

### Funktionsweise

Wir nehmen die aktuelle Geschwindigkeit der Drohne und transformieren sie in das Weltkoordinatensystem. Nun haben wir den Geschwindigkeitsvektor der Drohne v<sub>Drohne</sub>, welcher in der unternstehenden Abbildung eingetragen ist.

Zusammen mit dem Zielgeschwindigkeitsvektor v<sub>Ziel</sub> wird im zweiten Schritt die Ausgleichbewegung v<sub>Gegen</sub> bestimmt. 

v<sub>Gegen</sub> im Weltkoordinatensystem wird jetzt mit den Motoren (*roll*, *pitch*, *thrust*; *yaw* nicht benötigt) umgesezt.

![Koordinatensystem](pict_hover/3D-Koordinatensystem.png)

## 1. Schritt: Drohne zur Welt

Die Drohne ist ein sich frei im Raum bewegendes Objekt, welches sich auch gekippt um Raum (im folgenden Welt genannt) befinden kann. Alle Angaben, die wir zur Drohne über Sensoren erhalten sind relativ zur Drohnenposition und -neigung. Möchten wir zum Beispiel nun wissen, in welche Richtung die Drohne sich gerade bewegt, müssen wir den Geschwindigkeitsvektor (zusammengesetzt aus v<sub>Drohne;x</sub>, v<sub>Drohne;y</sub> und v<sub>Drohne;z</sub>) vom Drohnenkoordinatensystem in das Weltkoordinatensystem übersetzen.

### Theorie

Nach den Eulerschen Winkeln ergeben sich andere Transformationen, wenn man andere Winkel zuerst dreht. Die Drohne verwendet ein in der Fahrzeugtechnik gebräuchliches System des [" z, y', x'' "-Standards](http://de.wikipedia.org/wiki/Eulersche_Winkel#.E2.80.9Ez.2C_y.27.2C_x.27.27-Konvention.E2.80.9C_in_der_Fahrzeugtechnik). Sie besteht aus einer Neigung um *yaw*, *pitch *und *roll* in dieser Reihenfolge.

### Mathematik

Drehen wir vom Weltkoordinatensystem in das  Drohnenkoordinatensystem müssen wir folglich zuerst um die z-Achse (z; yaw), dann um die neue y-Achse (y'; pitch) und dann um die neue-neue x-Achse (x''; roll) drehen. Um diese Transformation rückgängig durchzuführen, müssen wir x also wiede zuerst zurück drehen (Messungen rückgängig gerade drehen). Daraus ergibt sich folgende Matrix (*yaw* entspricht *z*; *pitch* - *y*; *roll* - *x*):

![DrohneZuWelt](pict_hover/DrohneZuWelt.png)

Multipliziert man diese riesige Matrix mit einem Vektor im DKS ehält man diesen Vektor im WKS:

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

Die Rücktransformation findet analog zu Transformation Drohne-Welt.

BERECHNUNGEN HIER EINFÜGEN

Multiplizieren wir die folgende Matrix mit einem Vektor aus dem Weltkoordinatesystem, erhalten wir diesen Vektor im Drohnenkoordinatensystem:

BERECHNUNGEN HIER EINFÜGEN

### Umsetzug in Motren

Nun teilen wir den Vektor in die Bestandteile auf. v<sub>G;x</sub> übersetzen wir mit zusätzlichem *roll* - wir multipizieren v<sub>G;x</sub> mit einem Balancefaktor und addiren es zu unserem bisherigem *roll*. Gleiches Prinzip führen wir mit v<sub>G;y</sub> und *pitch* durch, sowie mit v<sub>G;z</sub> und *thrust*.

Als Balancefaktor haben wir bisher **noch keine für v<sub>G;x</sub> und v<sub>G;y</sub>** ausmachen können. Misst man alle 10ms, bietet sich allerdings **2500 für <sub>G;z</sub>** an.