# Erkenntnisse

1. positiv:
	- einfaches Steuern der Drohne über setPoint(roll, pitch, yawrate, thrust)
	- Sensoren sehr genau
2. negativ:
	- Loggingpakete nicht sendbar mit unter 10ms (Abfrage auf valid gibt false zurück)
	- Crazyflie wird von Wind und Rotation der Motoren beeinflusst ()
	- Thrust verändert sich mit Akkustatus (mehr Akku -> mehr Power)
	
3. neutral:
	- Beschleunigungsdaten werden in [g](http://de.wikipedia.org/wiki/G-Kraft) angegeben
	- Beschleunigungsachsen sind relativ zur Drohne (bei roll = 15° verändert sich die Beschleunigung in einzelnen Achsenrichtungen)
	-  Roll, Pitch, Yaw werden in Grad angegeben (für Steuerung doppelte Gradzahl)