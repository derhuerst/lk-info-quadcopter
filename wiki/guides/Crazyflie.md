# Crazyflie

## Steuerung der Drohne

### Drohne finden und Verbindung herstellen

```
cflib.crtp.init_drivers()
available = cflib.crtp.scan_interfaces()
for i in available:
	print "Interface with URI [%s] found and name/comment [%s]" % (i[0], i[1])

crazyflie = Crazyflie()
crazyflie.open_link("radio://0/10/250K")
# Do stuff
crazyflie.close_link()
```

### Control Commands

Diese control commands decken die wichtigstens und grundlegensten Methoden ab um die Drohne zu steuern.
Für den Fall, dass dies nicht ausreicht, muss mit Logging und Parametern gearbeitet werden, was deutlich komplexer ist.

```
roll    = 0.0
pitch   = 0.0
yawrate = 0
thrust  = 0
crazyflie.commander.send_setpoint(roll, pitch, yawrate, thrust)
```

roll und pitch werden als Winkel in Grad angegeben
thrust kann Werte zwischen 10001 und 60000 annehmen 

**Wichtig**
Wenn ein Befehl gesendet wird, wird dieser für 0.5 Sekunden ausgeführt, danach 
schaltet es sich wieder ab. Um auf einem konstanten thrust level zubleiben, 
sollten neue Befehle in möglichst kurzen Intervallen gesendet werden;
als ideal sind 100 Befehle pro Sekunde angegeben für eine sehr prezise Steuerung.

### Logging

Das Logging wird dazu benutzt um in festgelegten Intervallen Werte von der Drohne an den Client zu übermitteln,
sie werden nicht vom Client selbst verändert.

Um eine logging configuration zu erstellen wird folgender Code verwendet:

```
logconf = LogConfig("Logging", 100)
logconf.addVariable(LogVariable("group1.name1", "float"))
logconf.addVariable(LogVariable("group1.name2", "uint8_t"))
logconf.addVariable(LogVariable("group2.name1", "int16_t"))
```

In der ersten Zeile wird der Name der logging configuration und das Invtervall in dem die Daten gesendet werden in Millisekunden festgelegt (beides frei wählbar).
In den folgenden Zeilen werden die einzelnden Variablen hinzugefügt. Als erster Parameter wird der gewünschte Datensatz angeben, als zweites sein Datentyp. 
Diese sind beide NICHT frei wählbar. (Dazu später mehr)


Beispiel:

```
import logging
 
import cflib.crtp
from cfclient.utils.logconfigreader import LogConfig
from cfclient.utils.logconfigreader import LogVariable
from cflib.crazyflie import Crazyflie
 
logging.basicConfig(level=logging.DEBUG)
 
 
class Main:
    """
    Class is required so that methods can access the object fields.
    """
    def __init__(self):
        """
        Connect to Crazyflie, initialize drivers and set up callback.
 
        The callback takes care of logging the accelerometer values.
        """
        self.crazyflie = Crazyflie()
        cflib.crtp.init_drivers()
 
        self.crazyflie.connectSetupFinished.add_callback(
                                                    self.connectSetupFinished)
 
        self.crazyflie.open_link("radio://0/10/250K")
 
    def connectSetupFinished(self, linkURI):
        """
        Configure the logger to log accelerometer values and start recording.
 
        The logging variables are added one after another to the logging
        configuration. Then the configuration is used to create a log packet
        which is cached on the Crazyflie. If the log packet is None, the
        program exits. Otherwise the logging packet receives a callback when
        it receives data, which prints the data from the logging packet's
        data dictionary as logging info.
        """
        # Set accelerometer logging config
        accel_log_conf = LogConfig("Accel", 10)
        accel_log_conf.addVariable(LogVariable("acc.x", "float"))
        accel_log_conf.addVariable(LogVariable("acc.y", "float"))
        accel_log_conf.addVariable(LogVariable("acc.z", "float"))
 
        # Now that the connection is established, start logging
        self.accel_log = self.crazyflie.log.create_log_packet(accel_log_conf)
 
        if self.accel_log is not None:
            self.accel_log.data_received.add_callback(self.log_accel_data)
            self.accel_log.start()
        else:
            print("acc.x/y/z not found in log TOC")
 
    def log_accel_data(self, data):
        logging.info("Accelerometer: x=%.2f, y=%.2f, z=%.2f" %
                        (data["acc.x"], data["acc.y"], data["acc.z"]))
 
Main()
```

### Parameter

Parameter können vom Client direkt geändert werden:
```
# crazyflie is an instance of the Crazyflie class that has been instantiated and connected
crazyflie.param.setParamValue("led.freeze", True)
```

Man kann vom Client aus Parameter auch von der Drohne abfragen:
```
crazyflie = Crazyflie()
crazyflie.param.addParamUpdateCallback("led.freeze", paramUpdateCallback)
 
def paramUpdateCallback(name, value):
	print "%s has value %s" % (name, value) # This will in our example print: led.freeze has value True
```

Wie auch beim Logging gibt es festgelegte Parameter (also in diesem Beispiel led.freeze)

### Woher kriegen wir die vorgegebenen Parameter und Loggingdaten?

An dieser Stelle ergibt sich ein kleines Problem: die Parameter und Loggingdaten sind nicht direkt Teil der
Python Library, sondern sind Teil der Firmware der Drohne selbst, welche wir nicht direkt bearbeiten können.
Es ist uns also nicht möglich, eigene Parameter oder Loggingdaten der Drohne hinzuzufügen. 
Außerdem gibt es in der Hinsicht keine wirkliche Dokumentation in Hinsicht darauf, welche Parameter und Loggingwerte
zur Verfügung stehen. Nach langer Suche haben wir den Teil des Quellcodes der Firmware gefunden, in welcher die meisten
Parameter und Loggingdaten definiert werden. Für den Fall, dass Bedarf daran besteht diese einzusehen, haben wir aktuell keine
andere Möglichkeit, als uns durch den entsprechenden Quellcode zuwühlen, welcher [Hier](https://bitbucket.org/bitcraze/crazyflie-firmware/src//modules/src/) 
gefunden werden kann, vorallen in den Datein *controller.c* und *stabilizer.c*.


### Beispiel

Als anschauliches und leicht verständliches Beispiel würde ich [dieses](https://bitbucket.org/eldraco2000/crazyflie-programs/src/) Miniprojekt empfehlen.