# Erkenntnisse

1. positiv:
	- einfaches Steuern der Drohne über setPoint(roll, pitch, yawrate, thrust)
	- Sensoren sehr genau
2. negativ:
	- Loggingpakete nicht sendbar mit unter 10ms (Abfrage auf valid gibt false zurück)
	- Crazyflie wird von Wind und Rotation der Motoren beeinflusst ()
	- Thrust verändert sich mit Akkustatus (mehr Akku -> mehr Power)
	- Thrustspanne zwischen 10001 und 59999 (60000 führt zu Fehlern)
	- Versuch mit Waage fehlgeschlagen, die Ablage verändert Auftriebskraft: in der Luft fählt die drohne bei 34000 über der Waage steigt sie jedoch
	
3. neutral
	- Beschleunigungsdaten werden in [g](http://de.wikipedia.org/wiki/G-Kraft) angegeben
	- Beschleunigungsachsen sind relativ zur Drohne (bei roll = 15° verändert sich die Beschleunigung in einzelnen Achsenrichtungen)
	- Roll, Pitch, Yaw werden in Grad angegeben (für Steuerung doppelte Gradzahl)
	- wenn die Drohne auf dem Boden liegt, verändert sich die berechnete Geschwindigkeit im 0,001 bereich (gleiches gilt für bxeschleunigung) 
