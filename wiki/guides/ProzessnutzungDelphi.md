# Nutzung eines Pythonprogrammes in Delphi

##Das Pythonprogramm

Das hier verwendete Programm soll lediglich einen string erhalten und diesen sofort wieder ausgeben, anschließend wird das Programm wieder beendet.

```  
var = input(var)   # es ist an dieser Stelle auch möglich sys.stdIn.read zu nutzen, wenn man import system durchgeführt hat, allerdings ist der Unterschied nur, dass input noch ausgibt
print(var)         # print schreibt ebenfalls an die standardausgabe stdout und ermöglicht somit eine Rückgabe an Delphi
```

##Das Delphiprojekt

Dieses Programm hat die Aufgabe eine GUI zur Verfügung zu stellen, auf der der Benutzer einen text in ein editfeld schreibt, dieser an python geschickt wird. Anschließend holt sich Delphi die Pythonausgabe zurück und schreibt sie in ein Memofeld.

Um Prozesse nutzen zu können, muss man zuerst `Process` als unit in uses hinzufügen.  
Anschließend benötigt man Objekt für den Prozess, diese deklariert man mit  
`myProcess: TProcess`

Als nächstes muss der Prozess erstellt werden, wie man an folgendem Beispiel sieht:

```  
pyProcess:=TProcess.Create(nil); //Kreierung des Prozesses, Parameter nur für Elternklassen 'nil' geht bei uns immer  
{$IFDEF WINDOWS}// alles bis ENDIF wird nur ausgeführt, wenn ein Windows Betriebssystem genutzt wird  
pyProcess.Executable:={'C:\INFORMATIK\Python\Programm\}'python.exe';  //python starten   
{$ENDIF}  
{$IFDEF UNIX}  
pyProcess.Executable:='python.exe äquivalent in Linux';  
{$ENDIF}  
pyProcess.Parameters.add({'C:\INFORMATIK\Lazarus\Programme\ProcessProject\}'pythonAusAnfueger.py');  
//Parameter für die Ausführung: Auszuführendes Pythonprogramm angeben  
//Optionen für den Prozess sind Pipenutzung und verstecken der Konsole  
//Es gibt noch viele Optionen, die nicht notwendig sind  
//eventuell wird mal poWaitOnExit benötigt um auf Ende des Ausführung zu warten  
pyProcess.Options:= pyProcess.Options + [poUsePipes,poNoConsole];  
pyProcess.Execute;  
```

Um etwas zu übergeben, muss man es in die Pipe schreiben, dafür macht man dies:

```  
procedure TForm1.WriteToStream(instruction:string);  
var  
  buffer:array[0..511] of char;                                //characters zur Übergabe an Python  
begin  
  instruction:= instruction+#13#10;                            //Abschlusszeichen hinter den Befehl  
  strpcopy(buffer,instruction);                                //kopiere characters aus instruction in buffer  
  pyProcess.Input.Write(buffer,length(instruction));           //Kopiere alles aus instruction in den Input von pyProcess  
end;  
```

Um sich Daten zurückzuholen verwendet man:

```  
function TForm1.ReadFromStream(onlyLastline: boolean):string;  
var  
  readCount,lastLinePos :integer;  
  //readCount zählt die Anzahl der gelesenen bytes  
  //lastLinePos speichert das Ende der vorletzten Zeile  
  pyOut: array[0..511] of char;  //speichert den Output der Konsole  
begin  
  if (pyProcess.Output.NumBytesAvailable<>0) then   //Überprüfung, ob es eine Ausgabe gibt  
    begin  
      readCount:=pyProcess.Output.Read(pyOut,512);  
      //schreiben von bis zu 512 bytes von Python in pyOut, die Anzahl wird in readCount gespeichert  
      result:= Copy(pyOut,0,readCount);                            //Rückgabe nach konv. zu string  
      if (onlyLastLine) then                                       //wenn nur die letzte Zeile Result sein soll  
        begin  
          LastLinePos:= LastDelimiter(#13#10,result);  //Position des letzten Zeilenumbruchs finden  
          result:=Copy(result, lastlinePos,length(Result)-lastLinePos+1);//Ausgabe von allem, ab dem letzten Zeilenumbruch  
        end;  
    end;  
end;  
```

Man kann das Beenden des Prozesses auch erzwingen, mithlife von Terminate:  
```  
pyProcess.Terminate(0);          //beenden des Prozesses mit '0' da alles sauber geschlossen wurde  
```  

Bitte nicht vergessen den Destructor von TProcess aufzurufen, wenn man fertig ist.

[TProcess Interface]{http://lazarus-ccr.sourceforge.net/docs/fcl/process/tprocess.html}