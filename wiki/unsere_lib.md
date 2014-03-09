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

Hausaufgabe zum 11.03.14:

 - Wie sieht eine Schnittstelle beispielhaft aus?
 	- Allgemein
 	- Python-spezifisch
 - Von welchen Klassen erbt ein Baustein?￼

## Umsetzung in Python

**TODO** - Soll nach dem 11.03.14 ergänzt werden

Mit Stand vom 08.03.14 existieren zwei Vorschläge. Der erste von Jannis stammende Vorschlag enthält drei Basisbausteinklasse (0/1/n-Kinder) von der alle anderen Flugbewegungen unabhängig von der Schnittstelle erben. Die Unterscheidung der Schnittstellen an die Vaterklasse entsteht durch eine Art Identifikation, z.B. einen String. Es könnte dann in etwa wie folgt aussehen:

```python

class TBlock:
	type = ""
	allowed_type = ""
	
	def tick():
		pass
	
	...

class TBlockN(TBlock):
	child_list = []
	
	def addChild(self, child):
		if child.type = self.allowed_type:
			child_list.append(child)
		else:
			TypeError('Child is not the right type.')
			
	...
	
class TVKombinierer(TBlockN):
	type = "Vector"
	allowed_type = "Vector"
	
	...
```

Des Weiteren gab es noch einen andere Vorschlag von Sebastian, bei dem die Unterscheidung der Typen nicht durch Indentifikationsvariablen erreicht wird, sondern durch eine Vererbung, die es damit auch ermöglicht, eine Abfrage der Instanz zu machen. Benutzt wird hier die Pythons Funktionalität der Mehrfachvererbung. Es wäre auch möglich, das eine Flugbewegung zwei verschiedene Schnittstellen für mögliche Väter hat. Es kann, exemplarisch, einmal als eine an den Vater einen Vektor übergebene Flugbewegung und eine an den Vater RPYT übergebene Flugbewegung benutzt werden; zum Beispiel, falls eine Funktionalität mehrere Schnittstellen unterstützt oder sich intern beide Schnittstellen Hilfsmethoden teilen.

Dieser Vorschlag kam aufgrund semantischer Gründe, sowie Flexibilität bedingt besser an.

```python

class TBlock:
	pass
	
class TBlockN(TBlock):
	child_list = []
	
	def addChild(self, child):
		if accepted_instance(child):
			child_list.append(child)
		else:
			TypeError('Child is not the right type.')
			
	def accepted_instance(child):
		return False
		
	...
	
class TVectorBlock:
	
	def tick_vector():
		pass
		
	...
	
class TVKombinierer(TVectorBlock, TBlockN):
	
	def accepted_instance(child): # Überschreiben der Methode (Angabe, welche Instanzen Kinder sein dürfen
		return isinstance(child, TVectorBlock) # Dies ist unanhängig von der eigenen Vererbung
		
	def tick_vector(): # Implementation der Ticker-Methode
		pass # Damit der Vater diese Klasse ansprechen kann
		
	...
``` 

### Klassen & Objekte

**TODO** - Im Groben schon ergründet, keine konkreten Klassen(-diagramm)

### Schnittstellen

**TODO** - Erläuterung einzelner Schnittstellen und deren benötigte Methoden folgt... vielleicht...
