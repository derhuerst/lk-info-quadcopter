# Physikalische Berechnung

Die Berechnung der Geschwindigkeit in x,y,z Richtung mithilfe der Beschleunigungssensoren geschieht über die Zusammenrechnung der einzelnen Beschleunigungen (a) in bestimmten Intervallen (t, in unserem Fall 10ms). Diese Teilgeschwindigkeiten (a * t) werden mit der vorigen Gesamtgeschwindigkeit (v0) zu der neuen Gesamtgeschwindigkeit addiert (v).

Die benutze Formel: v= v0 + a * t


```python
speed_x += (acc_x - acc_x_default) * MAIN_TIMER
speed_y += (acc_y - acc_y_default) * MAIN_TIMER
speed_z += (acc_z - acc_z_default) * MAIN_TIMER
```