# Python

Python ist eine Konsolenanwendung und unterstützt nativ keine GUI. Die folgende Referenz bezieht sich auf Python 3.

- [Python3-Dokumentation](http://docs.python.org/3/) (englisch)
- [Python3-Dokumentation](http://openbook.galileocomputing.de/python/) (deutsch)
- [Schönes Python-Tutorial](http://www.learnpython.org/) (englisch)

## Grundstrukturen

### Kommentare

Python unterstützt nur einzeilige Kommentare.

```python
# Einzeiliger Kommentar
```

### Ausgabe

Die Ausgabe geschieht durch den Befehl ``print()``. Die Befehle werden nicht durch einen Zeilenumbruch separiert.

```python
print("Hallo Welt!")             # String
print(123)                       # Integer
print(input("Eingabe tätigen:")) # String aus einem Input (ReadLn)
```

```
Hallo Welt!
123
Eingabe tätigen: test
test
```

### Variablentypen/-zuweisung

```python
myint = 7
print(x)
myfloat = 7.0
print(x)
myfloat = float(7)
print(x)
mystring = 'String 1'
print(x)
mystring = "String 2 und schreib' ruhig Apostrophs"
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
summe = eins + zwei
print(summe)

hello = "Hello"
world = "World"
nachricht = hello + " " + world
print(nachricht)
print(hello, " ", world)

a, b = 4, 9
print(a+b)
```

```
3
Hello World
Hello World
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

### Operatoren

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
```

```
2
1
2.5
2.5
2
49
8
HalloHalloHalloHalloHallo
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
[2, 4, 6, 8, 1, 3, 5, 7]
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
Es ist eine Eins
Die Zahl gehört schon zu den Großen
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
