# Unsere Bibliothek

## Ziele & Anforderungen

Unsere Bibliothek soll die **Benutzung der cflib vereinfachen**. Sie soll dem Benutzer unserer lib **alle Möglichkeiten bieten**, die auch die cflib bietet.

Es existiert eine **Drohnenverwaltung** (im Weiteren *Drone*), die das Objekt der Crazyflie verwaltet, in regelmäßigen Abständen (geplant 10ms) nach neuen Werten fragt und diese an die das Crazyflie-Objekt sendet. 

Eine **Sensordatenverwaltung** (im Weiteren *Sensors*; Verwechselungsgefahr mit *Logging*) erstellt alle Sensorpakete bzw. die benötigten Pakete und speichert sie bei einem Callback-Update, sodass sie jederzeit für die Flugbewegungen zur Verfügung stehen.

Die **Flugbewegungen** (auch *Bausteine*) können verschiedene Rückgabe-/Übergabewerten haben. Jedes Übergabeprotokoll hat eine gemeinsame Schnittstelle.

Zudem soll es noch eine zusätzliche **zentrale Ausgabestelle** (im Weiteren *Logging*; Verwechsungsgefahr mit *Sensors*) zum Debuggen und Ausgeben geben. In verschiedenen Kategorien unterteilt können so Datei einfach in einem Logdatei gesammelt werden.

## Prinzipien

Daraus lässt sich folgendes Modell erstellen. Die Drohnenverwaltung erstellt eine *Sensors*-Instanz und eine *Logging*-Instanz und hat eine RPYT-Schnittstelle (hier *rund* dargestellt; im Gegensatz zu Vektoren *eckig*; weitere Schnittstellen nach gleichem Prinzip möglich) für Flugbewegungen.

![Klassenmodell](https://rawgithub.com/derhuerst/lk-info-quadcopter/master/wiki/pict_class_diagramm/class_model.svg)

Jede Flugbewegung hat genau einen Vater, an den er das aus den Kindern (je nach Flugbewegung 0-n Kinder) berechnete Ergebnis weiterleitet. So fragt die Elternklasse alle Kinder (also auch 0 möglich) über die Schnittstelle ein Ergebnis der Kinder ab.

Wird ein Kombinierer beispielsweise von seinem Vater nach einem Ergebnis gefragt, fragt dieser wiederum all seine Kinder nach deren Ergebnis, fügt diese zusammen und gibt dies an seinen Vater zurück.

![Plug-Modell](https://rawgithub.com/derhuerst/lk-info-quadcopter/master/wiki/pict_class_diagramm/plug_model.svg)

Hier zwei Beispiele, wie ein Baum während der Laufzeit zu einem bestimmten Zeitpunkt aussehen könnte:

![Strukturbeispiel während der Laufzeit (Normal)](https://rawgithub.com/derhuerst/lk-info-quadcopter/master/wiki/pict_class_diagramm/structure_example_normal.svg)

![Strukturbeispiel während der Laufzeit (Vektoren)](https://rawgithub.com/derhuerst/lk-info-quadcopter/master/wiki/pict_class_diagramm/structure_example_vector.svg)

## Klassendiagramm

**TODO** 

Hausaufgabe:

 - Wie sieht eine Schnittstelle beispielhaft aus?
 	- Allgemein
 	- Python-spezifisch
 - Von welchen Klassen erbt ein Baustein?￼

## Umsetzung in Python

Jeder Baustein erbt von ``TBlock``. Hat ein Block Kinder, erbt er stattdessen von der davon abgeleiteten Klasse ``TBlockN``, die zusätzlich noch eine Liste von Kindern ``child_list`` und eine Methode zum Hinzufügen in diese Liste ``def add_child():`` implementiert. Die Klasse ``TVectorBlock`` gibt an, welche Schnittstelle der Baustein an seinen Vater übergibt. Hier können zusätzliche Methoden (abstakt) implementiert werden können. Ein Baustein erbt also nicht nur von ``TBlock`` bzw. von ``TBlockN``, sondern auch von der Klasse, die die Schnittstelle *nach oben* angibt.

```python

class TBlock(object):
	
	def tick(self):
		pass
	
class TBlockN(TBlock):
	child_list = []
	
	def addChild(self, child):
		child_list.append(child)
		
	...
	
class TVectorBlock(object):
		
	...
	
class TVKombinierer(TVectorBlock, TBlockN):

	def add_child(self, child):
		if isinstance(child, TVectorBlock):
			super(TVectorBlock, self).add_child(child)
		else:
			TypeError(child.__class__.__name__ + " is not a possible child type.")
	
	def tick(self):
		pass      # Implementation der tick-Methode
		
	...
``` 

### Klassen & Objekte

**TODO** - Im Groben schon ergründet, keine konkreten Klassen(-diagramm)

### Schnittstellen

**TODO** - Erläuterung einzelner Schnittstellen und deren benötigte Methoden folgt... vielleicht...
