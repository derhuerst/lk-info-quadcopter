# Python

Python ist eine Konsolenanwendung und unterstützt nativ keine GUI. Die folgende Referenz bezieht sich auf Python 3.

[Wikipedia (Python)](http://de.wikipedia.org/wiki/Python_%28Programmiersprache%29):

> Python [ˈpaɪθn̩, ˈpaɪθɒn, auf Deutsch auch ˈpyːtɔn] ist eine universelle, üblicherweise interpretierte höhere Programmiersprache.[2] Ihre Entwurfsphilosophie betont Programmlesbarkeit.[3] Die Programmstruktur wird durch die Einrücktiefe gebildet. Andere Sprachen verwenden hierfür Klammern (C, JavaScript) oder Schlüsselwörter (Pascal).
>
>Python unterstützt mehrere Programmierparadigmen. So werden objektorientierte, aspektorientierte und funktionale Programmierung unterstützt. Wie andere dynamische Sprachen wird Python oft als Skriptsprache genutzt.
>
>Die Sprache hat ein offenes, gemeinschaftsbasiertes Entwicklungsmodell, gestützt durch die gemeinnützige Python Software Foundation, die de facto die Definition der Sprache in der Referenzumsetzung CPython pflegt.
>
>Python gilt als einfach zu erlernende Sprache, da sie über eine klare und übersichtliche Syntax verfügt.

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
        1. [Methoden](#methoden)
        2. [Klassendefinition](#klassendefinition)
        3. [Objektvariablen](#objektvariablen)
        4. [Vererbung](#vererbung)
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

Die   Ausgabe geschieht durch den Befehl ``print()``. Die Befehle werden nicht durch einen Zeilenumbruch separiert. Der Variablentyp als Parameter ist beliebig. Auch Objekte können übergeben werden, die mit einer Stringdarstellung angepasst werden können.

Falls mehrere Parameter angegeben werden, werden diese zu einem String zusammengefügt und ein Leerzeichen dazwischen hinzugeügt.

```python
print("Hallo Welt!")             # String
print(123)                       # Integer
print(123, 456)                  # Integer
print(input("Eingabe tätigen: ")) # String aus einem Input (ReadLn)
```

```
Hallo Welt!
123
123 456
Eingabe tätigen: test
test
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
String 1
String 2 und schreib' ruhig Apostrophs
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
print(hello, world)                  # Stringkontaktion durch Parameter bei print
```

```
3
Hello World
Hello World
13
```

### Listen

Listen sind spezielle [Objekte](#klassen--objekte) und Arrays mit zusätzlichen Funktionen. Um eine Liste (unten erklärt) als Stack zu benutzen, fügt man mit `liste.append(int)` zur Liste hinzu und entfernt (und erhält) das letzte Element mit `liste.pop()`. Auch kann eine Liste sortiert werden: `liste.sort()`. Um eine Lsite rückwärts zu sortieren gibt man ein sogenanntes *keyword argument* an: `liste.sort(reverse=False)`.

```python
liste = []        # Erstelle eine leere Liste.
liste.append(1)   # Füge hinten an die Liste eine 1 an.
liste.append(2)
liste.append(3)
print(liste[0])   # Gib das Element am Index 0 zurück.
print(liste[1])
print(liste[2])

print('')

liste = [1,2,3]    # Erstelle eine Liste mit 3 Listenelementen ([0] = 1, [1] = 2, [2] = 3)
print(liste[0])
print(liste[1])
print(liste[2])
print(liste)       # Gib die ganze Liste zurück.

print('')

print(liste.pop()) # Gib das letzte Listenelement zurück und entferne es aus der Liste.
print(liste)       # Gib die die Liste zurück, aus der das Element zuvor entfernt wurde.
```

```
1
2
3

1
2
3
[1, 2, 3]

3
[1, 2]
```

### Operationen

```python
zahl = 1 + 2*3/4      # Es gilt Punkt- vor Strichrechnung.
print(zahl)           # Die Division mit zwei ganzzahlen Operatioen (int) ergibt
zahl = 1 + 2/4*3      # ein ganzzahliges Ergebnis (immer abgerundet; Pascal
print(zahl)           # DIV-Äquivalent. Ist ein/zwei Operator nicht ganzzalig,
zahl = 1 + 2*3/4.0    # ist das Ergebnis auch nicht ganzzahlig (Float-Division).
print(zahl)
zahl = 1 + 2/4.0*3
print(zahl)

print('') # -------------------------

rest = 11 % 3         # Der Rest kann mit dem Modulo-Zeichen (%) errechnet werden.
print(rest)

quadrat = 7 ** 2      # Potenzen werden mit zwei Sternchen angegeben.
print(quadrat)

hoch3 = 2 ** 3
print(hoch3)

wurzel = 2 ** 0.5     # Wurzeln können neben dieser Möglichkeit auch durch die Wurzel-
print(wurzel)         # funktion im Math-Modul berechnet werden, die je nach Interpreter
                      # schneller oder langsamer sind.

print('') # -------------------------

vieleHallo = "Hallo" * 5                              # Den String n-mal hintereinander
print(vieleHallo)

vieleZahlen = [1, 2, 3] * 5                           # Die Liste n-mal hintereinander
print(vieleZahlen)

gerade_zahlen = [2, 4, 6, 8]
ungerade_zahlen = [1, 3, 5, 7]
alle_zahlen = gerade_zahlen + ungerade_zahlen         # Fügt Liste-2 an Liste-1 hinzu
print(alle_zahlen)
alle_zahlen.sort()                                    # EXKURS: Bringt die Zahlen in die
print(alle_zahlen)                                    # richtige Reihenfolge

print('') # -------------------------

print(str(10))                                        # Konvertiert einen Integer zu einem String
print(int('10'))                                      # Konvertiert einen String zu einem Integer
print(str(quadrat)+' ist das Quadrat von sieben.')    # Nur gleiche Variablentypen können
print(quadrat, 'ist das Quadrat von sieben.')         # "addiert" werden.
```

```
2
1
2.5
2.5

2
49
8
1.4142135623730951

'HalloHalloHalloHalloHallo'
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
[2, 4, 6, 8, 1, 3, 5, 7]
[1, 2, 3, 4, 5, 6, 7, 8]

'10'
10
49 ist das Quadrat von sieben.
49 ist das Quadrat von sieben.
```

### Kontrollstrukturen

#### Bedingungen

Es gibt in Python keine `case`/`switch`-Anweisungen. Stattdessen müssen lange if-anweisungen benutzt werden. Es können mehrere `elif`-Statements verwendet werden. Bei Vergleichen muss der Variablentyp übereinstimmen. Ansonsten sind sie nicht gleich.

```python
x = 1
if (x == 1):
    print("Es ist eine Eins")
elif (x == 2):
    print("Zwei")
else:
    print("Kenne ich nicht")

x = 6
if (x >= 6):                                       # == Wer und Variablentyp gleicht. Bei Objekten die Adresse.
    print("DIE ZAHL GEHÖRT SCHON ZU DEN GROßEN!")  # != Wer oder Variablentyp gleicht nicht. Bei Objekten die Adresse.
elif (x == 6):                                     # >= a größer/gleich b  (auch bei Strings Zeichen für Zeichen nach ASCII)
    print("Keiner mag mich! :(")                   # <= a kleiner/gleich b (                       "                       )
elif (x == 6):                                     # >  a größer         b (                       "                       )
    print("Ich bin besser als die Sexs...")        # <  a kleiner        b (                       "                       )
else:
    print("ich kümmere mich un die kleinen")
```

```
Es ist eine Eins
Die Zahl gehört schon zu den Großen
```

#### Schleifen

In Python gibt es zwei Arten von Schleifen: `while`- und `for`-Schleifen.

```python
secret = "1337" 
guess = "0"
while (guess != secret):
    guess = input("Raten Sie: ") 
print("Sie haben es geschafft!")

print('') # -------------------------

for i in range(5):                #range(stop)
    print(i)

print('') # -------------------------

for i in range(3,5):              #range(start, stop)
    print(i)

print('') # -------------------------

for i in range(10,1, -2):         #range(start, stop, step)
    print(i)
```

```
Raten Sie: 100
Raten Sie: 200
Raten Sie: 1337 
Sie haben es geschafft!

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

Der einzige Mapping-Datentyp von Python ist ein Dictionary, also ein Wörterbuch. In anderen Programmiersprachen heißt er *assoziatives Array*, *Map* oder *Hash*. Ein Dictionary enthält belibig viele Schlüssel-Wert-Paare. 

```python
dict = {'Name': 'Zara', 'Alter': 7, 'Klasse': 'Erste'}

print("Name:", dict['Name'])
print("Alter:", dict['Alter'])

dict['Alter'] = 5
print("Alter:", dict['Alter'])
```

```
Name: Zara
Alter: 7
Alter: 5
```

## Objekt-Orientiert

### Methoden

Methoden werden durch das Stichwort `def` eingeleitet. Eine Funktion kann auch aufgerufen werden, wenn die Deklaration weiter unter steht.

```python
meine_funktion()                            # Der Aufruf der Funktion vor der Deklaration

def meine_funktion():                       # Deklaration meine_funkion()
    print("Hallo von meiner Funktion!")     # RETURN OHNE RÜCKGABEWERT IST OPTIONAL
    return                                  # ABER NICHT STYLEGUIDEKONFORM
    
meine_funktion()                            # Erneuter Aufruf der Funktion

def meine_funktion_args(name, gruss):       # Hier wurde kein >return< angegeben
    print("Hallo", name, "von meiner Funktion! Ich wünsche dir", gruss)

meine_funktion_args("Hans", "Viel Erfolg!") # Aufruf einer Punktion mit Parametern
meine_funktion_args("Lara", "Viel Spaß!")   # ...und mit anderen Parametern

def geheimeformel(a):                       # Diese Methode gibt etwas zurück
    return a*3 + 2                          # Rückgabewert (logischerw. n. optional)

print(geheimeformel(5))                     # Aufruf und Ausgabe der Formel
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

Ein **Konstruktor** ist eine Methode, die den Namen `__init__` trägt. Der Konstruktor dient dazu, Variablen (Integer, Strings, Objekte, Files, ...) vorzubelegen, die später innerhalb mehrerer Methoden innerhalb der Klasse benutzt werden (Klassenvariablen). Dazu zählt auch die Erstellung anderer Objekte oder das Öffnen von Files.

Die **Destruktormethode** heißt `__del__` und dient dazu Klassenobjekte zu schließen (nicht freizugeben). Also zum Bleistift das schießen von Files (`f.close()`). Anders als bei Delphi müssen keine Objekte zerstört werden. 

Der **garbage collector** sammelt in Python alle nicht mehr benötigten Objekte auf und gibt sie frei. Falls der Objektreferenzzähler 0 wird, wird nach dem Aufruf des Destruktors der Speicherplatz des Objekts freigegeben. Diese Form des GC ist relativ billig. Einer der größten Kosten sind die zusätzlichen Speicherplatzresourcen. Ein Integer benötigt so 12 Bytes (immer etwa 8 Byte mehr) - zeitlich kaum ein Unterschied (< +4%).

```python
class TMonty:


    def __init__(self,var):             # Konstruktor
        self.meine_variable = var       # Erstellen der Klassenvariable meine_variable
        f = open('text_file.txt', a)    # Textfile wird geöffnet
 
    def __del__(self):                  # Destruktor (Autom. Aufruf des Garbage Collector
        f.close()                       # Schließen des Files

    def meine_methode(self):            # Definition der Methode
        print(self.meine_variable)
```

#### Objektvariablen

Ein Konstruktoraufruf findet durch eine Zuweisung statt, wobei auf der linken Seite der Klassenname mit Parametern steht (ohne self). Danach zeigt die Variablenreferent auf ein Objekt dieser Klasse.

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
        TMonty.__init__(self, var)     # Aufruf des Konstruktors der Vaterklasse
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
    pass
```
- Jede Zeile hat höchstens 79 Zeichen.
- Toplevel-Funktionen und Klassendeklarationen werden mit zwei Leerzeilen getrennt.
- Methodendefinitionen innerhalb einer Klasse werden mit einer Leerzeile getrennt.
- Wir vereinbaren, dass wir Module, Klassen und Methoden immer nach folgendem Muster beschreiben

```python
# Snakes
# This module inherits many snake types. Description bla, bli, blub.
# 
# Classes:
# - TPython
# - TOtherSnake

import time


class TPython:
    # This class has a description, too.
    # 
    # Methods:
    # - schlangenlaenge()
    #   RETURN: length of the python snake. (int)
    # - draw_as_ascii_art(file)
    #   * file - (type: file) File with the drawing - have to be open in append mode
    #   Draws the Snake in the file
    # 
    # Public variables:
    # - varname
    #   description here
    # - var2
    #   another desc
    # 
    # Protected variables:
    # - _inheritance_only
    #   description here
    # - _luke_i_am_your_father
    #   Darth Vader is telling to Luke
    
    def schlangenlaenge(self):
        return _laenge * __le

    def draw_to_file_as_ascii_art(self, file):
        pass
```

- Leerzeilen sollen verwendet werden um logische Sektionen innerhalb von Funktionen voneinander zu trennen.
- Der Code sollte in Englisch geschrieben werden, wann immer es sinnvoll ist.

### Whitespaces

Keine zusätzlichen Leerzeichen ...

- ...innerhalb von Klammern  

```python
#JA:
spam(ham[1], {eggs: 2})

#NEIN:
spam( ham[ 1 ], { eggs: 2 } )
```
- ...vor einem Komma, Semikolon oder Punkt  

```python
#JA:
if x == 4: print x, y; x, y = y, x

#NEIN:
if x == 4 : print x , y ; x , y = y , x
```
- ...vor Klammern, die eine Parameterliste oder eine Indexliste starten.

```python
#JA:
x = fibb(array[5])

#NEIN:
x = fibb (array [5])
```
- ...als 1 um eine Zuweisung oder ähnliches, um mit anderem aus einer Höhe zu sein.

```python
#JA:
a = 5
b = 6
langes_c = 2

#NEIN:
a =        5
b =        6
langes_c = 2
```

### Kommentare
- Der Code soll gründlich auskommentiert sein.
- Kommentare sollten Englisch sein, wenn es sinnvoll ist.
- Kommentarblöcke sollten sich auf der selben Ebene wie der folgende von ihnen beschriebene Code befinden. Jede Zeile eines Kommentarblocks beginnt mit '#' gefolgt von einem Leerzeichen. Paragraphen innerhalb eines Kommentarblocks werden mit einer Zeile getrennt, die nur ein '#' enthält.

```python
# Dies ist
# ein Kommentarblock.
#
# Er enthält
# einen Absatz.
```
- Kommentare in der selben Zeile sollten möglichst selten verwendet werden. Sie werden durch mindestens zwei Leerzeichen vom voranstehenden Code getrennt. Sie beginnen mit '#' gefolgt von einem einzigen Leerzeichen.

```python
pass  # Dies ist ein Inlinekommentar.
```

### Namenskonventionen

[Python](http://www.python.org/dev/peps/pep-0008/#naming-conventions) kann es auch nicht besser :

> The naming conventions of Python's library are a bit of a mess, so we'll never get this completely consistent -- nevertheless, here are the currently recommended naming standards.

- Klassennamen beginnen grundsätzlich mit einem T und jedes darauf folgende Wort wird großgeschrieben. Bsp.: ``class TSomeClass:``
- Methoden-, Methodenparameter- und Variablenbezeichner werden kleingeschrieben und einzelne Worte durch `_` getrennt. Bsp.: `def a_small_method(a_integer_parameter):` `a_variable = 7`
- Konstanten werden komplett großgeschrieben und einzelne Worte durch `_` getrennt. Bsp.: `CONST_EXAMPLE = "Example"`
- Bei Vererbung haben öffentliche Attribute keinen vorangestellten Unterstrich. Attribute, die nur vererbt werden solle, habenn einen Unterstrich vor dem Namen. Attribute die nicht vererbt werden sollen, haben zwei Unterstriche vor dem Namen.  
Anmerkung: _Die Unterstriche haben allerdings keine Bedeutung für Python. Es sind alle Methoden/Variablen verfügbar._  
Bsp.:

```python
class TExampleClass:


    def public():
        pass

    def _protected():
        pass

    def __private():
        pass
```

### Sonstiges

- Vor und hinter jedem binären Operator, wie (erweierte) Zuweisungen (`=`, `+=`, `-=`, etc.), Vergleiche (`==`, `<`, `>`, `!=`, `<=`, `>=`, `in`, `not in`, `is`, `is not`) oder boolean'schen Operatoren (`and`, `or`, `not`) müssen Leerzeichen stehen und um den Ausdruck Klammern. Bsp.: `if (a == b):`
- Falls Operatoren mit verschiedenen Operatoren benutzt werden, wird der Operator mit der geringeren Priorität mit einem Leerzeichen auf beiden Seiten umgeben (`x = x*2 - 1`, `hypot2 = x*x + y*y`, `c = (a+b) * (a-b)`).
- Keine mehreren Anweisungen in eine Zeile (**NICHT** `do_one(); do_two(); do_three()`).
- Benutzt nur `a != b`, statt `a <> b` oder `not (a == b)`

## Unit-Verwaltung

In Python können Module (Datei im gleichen Ordner) entweder einzeln oder als ganzes Paket (Unterordner) importiert werden.
Üblichwerweise wird, um Namenskonflikten aus dem Weg zu gehen, der Namensraum nicht mit übertragen.
Somit müssen sämtliche Methode, Klassen, Variablen etc. mit `Dateiname.Klasse_Methode` bzw.
`Paketname.Dateiname.Klasse_Methode` angesprochen werden.
Ein Paket ist ein mit Modulen gefüllter Ordner der zusätzlich ein ``__init__.py`` Modul enthält. Dieses Modul kann leer sein. 

```python
import Modul                          # Importiert gesamten Inhalt einer Modul
import sys                            # Importiert Pythoninternes Modul sys
sys.path.insert(0, 'C:\DateiOrdner')  # Fügt DateiOrdner dem von 'import' durchsuchten Pfad hinzu
import Modul as file                  # Importiert und ändert Namensraum zu file

import Paket.*                        # Importieren eines gesamten Paketes


from PaketZwei import Modul           # Importiert nur ein Modul eines Pakets
```

## IDE

Die IDE ist auf der offiziellen Website zu finden. Wir benutzen allerdings nur den Compiler.

### Installation

1. Sucht euch auf der [offiziellen Downloadseite](http://www.python.org/download/) die neuste Version von Python 3 für euer Betriebssystem herunter (momentan 3.3.3)
2. Installiert Python3
    1. Unter Windows unter `C:/Python33` (Standard)
    2. Aktiviert das Feature "_Add python.exe to Path_"

### Verwendung

1. Schreibt `print("Hallo Welt")` in ein Textfile und speichert sie als `beliebigerName.py`.
2. Führt mit ener beliebigen Konsole den Befehl `python "Pfad\zur\Datei\beliebigerName.py"`

### Integrierung in Windows - *.bat

Das ist eigentlich ziemlich einfach. Man schreibt einfach die obige Zeile in eine *.bat und damit das Ergebnis sichtbar bleibt `pause` dahinter:

```bat
python "Pfad/zur/Datei.py
pause
```
