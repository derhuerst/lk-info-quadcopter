# Python
 
Python ist eine Konsolenanwendung und unterstützt nativ keine GUI. Die folgende Referenz bezieht sich auf Python 3.
 
- [Python3-Dokumentation](http://docs.python.org/3/) (englisch)
- [Python3-Dokumentation](http://openbook.galileocomputing.de/python/) (deutsch)
- [Styleguide](http://www.python.org/dev/peps/pep-0008/) (englisch)
 
Gliederung:
 
1. [Grundstrukturen](#grundstrukturen)
    1. [Kommentare](#kommentare)
    2. [Ausgabe](#ausgabe)
    3. [Variablentypen/-zuweisung](#variablentypen-zuweisung)
    4. [Operatoren](#operatoren)
    5. [Listen](#listen)
    6. [Operationen](#operationen)
    7. [Kontrollstrukturen](#kontrollstrukturen)
        1. [Bedingungen](#bedingungen)
        2. [Schleifen](#schleifen)
    8. [Dictionaries](#dictionaries)
    9. [Klassen & Objekte](#klassen--objekte)
        1. [Klassendefinition](#klassendefinition)
        2. [Objektvariablen](#objektvariablen)
        3. [Vererbung](#vererbung)
2. [Python-Styleguide](#python-styleguide)
    1. [Codelayout](#codelayout)
    2. [Whitespaces](#whitespaces)
    3. [Kommentare](#kommentare)
    4. [Namenskonventionen](#namenskonventionen)
    5. [Sonstiges](#sonstiges)
3. [Unit-Verwaltung](#unit-verwaltung)
4. [IDE](#ide)
    1. [Installation](#installation)
    2. [Verwendung](#verwendung)
    3. [Integrierung in Windows - *.bat](#integrierung-in-windows---bat)
 
## Grundstrukturen
 
### Kommentare
 
Python unterstützt nur einzeilige Kommentare.
 
```python
# Einzeiliger Kommentar
```
 
### Ausgabe
 
Die   Ausgabe geschieht durch den Befehl ``print()``. Die Befehle werden   nicht durch einen Zeilenumbruch separiert. Der Dateityp als Parameter ist beliebig. Auch Objekte können übergeben werden, wenn sie eine   Stringdarstellung besitzen.
Falls mehrere Parameter angegeben werden, werden diese zu einem String zusammengefügt.
 
```python
print("Hallo Welt!")             # String
print(123)                       # Integer
print(123, 456)                  # Integer
print(input("Eingabe tätigen:")) # String aus einem Input (ReadLn)
```
 
```
'Hallo Welt!'
123
123456
Eingabe tätigen: test
'test'
```
 
### Variablentypen/-zuweisung
 
Der Dateityp einer Variable wird durch die Zuweisung festgelegt.
 
```python
myint = 7                                              # Integer
print(x)
myfloat = 7.0                                          # Float
print(x)
myfloat = float(7)                                     # Float
print(x)
mystring = 'String 1'                                  # String
print(x)
mystring = "String 2 und schreib' ruhig Apostrophs"    # String
print(x)
```
 
```
7
7.0
7.0
'String 1'
'String 2 und schreib' ruhig Apostrophs'
```
 
### Operatoren
 
```python
eins = 1
zwei = 2
summe = eins + zwei                  # "+" als Addition
print(summe)
 
hello = "Hello"
world = "World"
nachricht = hello + " " + world      # "+" als Stringkontaktion
print(nachricht)
print(hello, " ", world)             # Stringkontaktion durch Parameter bei print
```
 
```
3
'Hello World'
'Hello World'
13
```
 
### Listen
 
```python
liste = []
liste.append(1)
liste.append(2)
liste.append(3)
print(liste[0])
print(liste[1])
print(liste[2])
 
liste([1,2,3])
print(liste[0])
print(liste[1])
print(liste[2])
```
 
```
1
2
3
1
2
3
```
 
### Operationen
 
```python
zahl = 1 + 2 * 3 / 4
print(zahl)
zahl = 1 + 2 / 4 * 3
print(zahl)
zahl = 1 + 2 * 3 / 4.0
print(zahl)
zahl = 1 + 2 / 4.0 * 3
print(zahl)
 
rest = 11 % 3
print(rest)
 
quadrat = 7 ** 2
print(quadrat)
 
hoch3 = 2 ** 3
print(hoch3)
 
vieleHallo = "Hallo" * 5
print(vieleHallo)
 
vieleZahlen = [1, 2, 3] * 5
print(vieleZahlen)
 
gerade_zahlen = [2, 4, 6, 8]
ungerade_zahlen = [1, 3, 5, 7]
alle_zahlen = gerade_zahlen + ungerade_zahlen
print(alle_zahlen)
 
print(str(10))
print(int('10'))
print(str(quadrat)+' ist das Quadrat von sieben.')
print(quadrat, 'ist das Quadrat von sieben.')
```
 
```
2
1
2.5
2.5
2
49
8
'HalloHalloHalloHalloHallo'
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
[2, 4, 6, 8, 1, 3, 5, 7]
'10'
10
49 ist das Quadrat von sieben.
49 ist das Quadrat von sieben.
```
 
### Kontrollstrukturen
 
#### Bedingungen
 
```python
x = 1
if (x==1):
    print("Es ist eine Eins")
elif (x==2):
    print("Zwei")
else:
    print("Kenne ich nicht")
    
x = 6
if (x>=6):
    print("Die Zahl gehört schon zu den Großen")
elif (x==6):
    print("Keiner mag mich!")
else:
    print("Ich kümmere mich um die Kleinen")
```
 
```
'Es ist eine Eins'
'Die Zahl gehört schon zu den Großen'
```
 
#### Schleifen
 
```python
secret = 1337 
guess = 0 
while (guess != secret): 
    guess = input("Raten Sie: ") 
print("Sie haben es geschafft!")
 
print("")
 
for i in range(5):          #range(stop)
    print(i)
 
print("")
 
for i in range(3,5):        #range(start, stop)
    print(i)
 
print("")
 
for i in range(10,1, -2):   #range(start, stop, step)
    print(i)
```
 
```
Raten Sie: 100
Raten Sie: 200
Raten Sie: 1337 
'Sie haben es geschafft!'
 
0
1
2
3
4
 
3
4
 
10
8
6
4
2
```
 
### Dictionaries
 
```python
dict = {'Name': 'Zara', 'Alter': 7, 'Klasse': 'First'};
print("Name: ", dict['Name']);
print("Alter: ", dict['Alter']);
print("Gewicht: ", dict['Gewicht']);
```
 
```
dict['Name']:  Zara
dict['Alter']:  7
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'
```
 
## Objekt-Orientiert
 
### Funktionen
 
```python
meine_funktion()
 
def meine_funktion():
    print("Hallo von meiner Funktion!")
    
meine_funktion()
 
def meine_funktion_args(name, gruss):
    print("Hallo ", name, " von meiner Funktion! Ich wünsche dir ", gruss)
 
meine_funktion_args("Hans", "Viel Erfolg!")
meine_funktion_args("Lara", "Viel Spaß!")
 
def geheimeformel(a):
    return a*3+2     #Rückgabewert
 
print(geheimeformel(5))
```
 
```
Hallo von meiner Funktion!
Hallo von meiner Funktion!
Hallo Hans von meiner Funktion! Ich wünsche dir Viel Erfolg!
Hallo Lara von meiner Funktion! Ich wünsche dir Viel Spaß!
17
```
 
### Klassen & Objekte
 
#### Klassendefinition
 
Eine Klassenmethode **benötigen** ``self`` als *ersten* Parameter, wenn innerhalb dieser Klassenmethode eine beliebige Klassenmethoden oder -variablen benutzt werden. Werden innerhalb dieser Klassenmethode keine Klassenmethoden oder -variablen keine benutzt, ist der Parameter ``self`` **optional**. 
 
```python
class TMonty:
 
 
    def __init__(self,var):             # Konstruktor
        self.meine_variable = var       # Erstellen der Klassenvariable meine_variable
 
    def meine_methode(self):            # Definition der Methode
        print(self.meine_variable)
```
 
#### Objektvariablen
 
```python
mein_objekt = TMonty(13)        # Erstellen des Objekts
mein_objekt.meine_methode()     # Aufrufen der Objektmethode
```
 
 
```
13
```
 
#### Vererbung
 
```python
class TPython(TMonty):
 
 
    def __init__(self, var, laenge):
        TMonty.__init__(self, var)
        self.laenge = laenge
 
    def schlangenlaenge(self):
        return str(self.laenge)+" Meter"
 
anderes_objekt = TPython(7,25)
anderes_objekt.meine_methode()
print(anderes_objekt.schlangenlaenge())
 
```
 
## Python-Styleguide
 
### Codelayout
 
- Einrückungen betragen 4 Leerzeichen.
```python
if indentation == 4:
    dosomething()
```
- Jede Zeile hat höchstens 79 Zeichen.
- Klassen und Methoden werden mit zwei Leerzeichen getrennt.
- Methoden Definitionen innerhalb einer Klasse werden mit einer Leerzeile getrennt.
```python
class MyClass:
 
 
    def dosomething():
        pass
 
    def doanything():
        pass
```
 
- Leerzeilen sollen verwendet werden um logische Sektionen innerhalb von Funktionen voneinander zu trennen.
- Der Code sollte in Englisch geschrieben werden, wann immer es sinnvoll ist.
 
 
### Whitespaces
 
Keine zusätzlichen Leerzeichen ...
 
- ...innerhalb von Klammern  
  ``JA:   spam(ham[1], {eggs: 2})``  
  ``NEIN: spam( ham[ 1 ], { eggs: 2 } )``
- ...vor einem Komma, Semikolon oder Punkt  
  ``JA:   if x == 4: print x, y; x, y = y, x``  
  ``NEIN: if x == 4 : print x , y ; x , y = y , x``
- ...vor Klammern, die eine Parameterliste oder eine Indexliste starten  
  ``JA:   x = fibb(array[5])``  
  ``NEIN: x = fibb (array [5])``
- ...als 1 um eine Zuweisung oder ähnliches, um mit anderem aus einer Höhe zu sein.
```python
    #JA:
    a = 5
    b = 6
    langes_c = 2
```
```python
    #NEIN:
    a =        5
    b =        6
    langes_c = 2
```
 
### Kommentare
- Der Code soll gründlich auskommentiert sein.
- Kommentare sollten Englisch sein, wenn es sinnvoll ist.
- Kommentarblöcke sollten sich auf der selben Ebene wie der folgende von ihnen beschriebene Code befinden. Jede Zeile eines Kommentarblocks beginnt mit '#' gefolgt von einem Leerzeichen. Paragraphen innerhalb eines Kommentarblocks werden mit einer Zeile getrennt, die nur ein '#' enthält
```python
# Dies ist
# ein Kommentarblock.
#
# Er enthält
# einen Absatz.
```
- Kommentare in der selben Zeile sollten möglichst selten verwendet werden. Sie werden durch mindestens zwei Leerzeichen vom voranstehenden Code getrennt. Sie beginnen mit '#' gefolgt von einem einzigen Leerzeichen.
```python
pass  # Dies ist ein Inline Kommentar.
```
 
### Namenskonventionen
 
[Python](http://www.python.org/dev/peps/pep-0008/#naming-conventions) kann es auch nicht besser :
 
> The naming conventions of Python's library are a bit of a mess, so we'll never get this completely consistent -- nevertheless, here are the currently recommended naming standards.
 
- Klassennamen beginnen grundsätzlich mit einem T und jedes darauf folgende Wort wird großgeschrieben. Bsp.: ``class TSomeClass:``
- Methoden-, Methodenparameter- und Variablenbezeichner werden kleingeschrieben und einzelne Worte durch '_' getrennt. Bsp.:``def a_small_method(a_integer_parameter):`` ``a_variable = 7``
- Konstanten werden komplett großgeschrieben und einzelne Worte durch '_' getrennt. Bsp.: ``CONST_EXAMPLE = "Example"``
- Bei Vererbung haben öffentliche Attribute keinen vorangestellten Unterstrich. Attribute die nur vererbt werden sollen einen Unterstrich vor dem Namen. Attribute die nicht vererbt werden sollen zwei Unterstriche vor dem Namen. Bsp.
```
class TExampleClass:
 
 
    def public():
        pass
 
    def _protected():
        pass
 
    def __private():
        pass
```
 
### Sonstiges
 
- Vor jeden binären Operator, wie (erweierte) Zuweisungen (``=``, ``+=``, ``-=``, etc.), Vergleiche (``==``, ``<``, ``>``, ``!=``, ``<=``, ``>=``, ``in``, ``not in``, ``is``, ``is not``) oder boolean'schen Operatoren (``and``, ``or``, ``not``).
- Falls Operatoren mit verschiedenen Operatoren benutzt werden, wird der Operator mit der geringeren Priorität mit einem Leerzeichen auf beiden Seiten umgeben (``x = x*2 - 1``, ``hypot2 = x*x + y*y``, ``c = (a+b) * (a-b)``).
- Keine mehreren Anweisungen in eine Zeile (**NICHT** ``do_one(); do_two(); do_three()``).
- Benutzt nur ``a != b``, statt ``a <> b`` oder ``not (a == b)``
 
## Unit-Verwaltung
 
In Python können Module (Datei im gleichen Ordner) entweder einzeln oder als ganzes Paket (Unterordner) importiert werden.
Üblichwerweise wird, um Namenskonflikten aus dem Weg zu gehen, der Namensraum nicht mit übertragen.
Somit müssen sämtliche Methode, Klassen, Variablen etc. mit Dateiname.Klasse_Methode bzw.
Paketname.Dateiname.Klasse_Methode angesprochen werden.
Ein Paket ist ein mit Modulen gefüllter Ordner der zusätzlich ein ``__init__.py`` Modul enthält. Dieses Modul kann leer sein. 
 
```
import Modul                          # Importiert gesamten Inhalt einer Modul
import sys                            # Importiert Pythoninternes Modul sys
sys.path.insert(0,'C:\DateiOrdner')   # Fügt DateiOrdner dem von 'import' durchsuchten Pfad hinzu
import Modul as file                  # Importiert und ändert Namensraum zu file
 
import Paket.*                        # Importieren eines gesamten Paketes
 
 
from PaketZwei import Modul           # Importiert nur ein Modul eines Pakets
```
 
## IDE
 
Die IDE ist auf der offiziellen Website zu finden. Wir benutzen allerdings nur den Compiler.
 
### Installation
 
1. Sucht euch auf der [offiziellen Downloadseite](http://www.python.org/download/) die neuste Version von Python 3 für euer Betriebssystem herunter (momentan 3.3.3)
2. Installiert Python3
    1. Unter Windows unter ``C:/Python33`` (Standard)
    2. Aktiviert das Feature "Add python.exe to Path"
 
### Verwendung
 
1. Schreibt ``print("Hallo Welt")`` in ein Textfile und speichert sie als ``beliebigerName.py``.
2. Führt mit ener beliebigen Konsole den Befehl ``python "Pfad\zur\Datei\beliebigerName.py"
 
### Integrierung in Windows - *.bat
 
Das   ist eigentlich ziemlich einfach. Man schreibt einfach die obige Zeile   in eine *.bat und damit das Ergebnis sichtbar bleibt ``pause`` dahinter:
 
```
python "Pfad/zur/Datei.py
pause
```
