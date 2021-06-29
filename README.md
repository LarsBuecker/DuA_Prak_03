
# DuA_Prak_03

DuA Praktikum - Aufgabe 3

  

## Requirements

- Textdatei mit ungerichteten Graphen in Form von Adjazenzlisten mit gewichteten Kanten einlesen
- Kantengewichte: Ganze Zahlen {1,...,10000}
- Minimum Spanning Tree (MST) Problem lösen
- Ausgabe: ungerichteter Graph mit Kantengewicht in Konsole
- Kruskal-Algorithmus Implementieren
- Für sortierung dürfen Bibliotheken genutzt werden


### Eingabeformat
\<Kommentarzeile>
...
\<Kommentarzeile>
n = \<ganze  Zahl>
\<nr> : \<Adjazenzliste>
...
\<nr> : \<Adjazenzliste>


Kommentarzeilen beginnen mit #
n = ... gibt die Anzahl der Knoten des Graphen an.
Es folgen die Adjazenzlisten der Startknoten \<nr>, diedurch \<Leerzeichen>:\<Leerzeichen> vom Startknoten getrennt sind. Eine \<Adjazenzliste> ist eine durcheinzelne Leerzeichen getrennte Listevon \<Kanten>, eine \<Kante> bestehtaus \<nr>w\<gewicht>, wobei\<nr>eineKnotennummer ist und \<gewicht> das Kantengewicht als ganze Zahlist. Knotennummer und Kantengewichtwerden durch das Zeichenwgetrennt.Da der Graph ungerichtet ist, erscheintjede Kante zweimal in den Adjazenzlis-ten.

### Ausgabeformat
Die Ausgabe des Spannbaums als ungerichteter Graph entsprechend zum Eingabeformat (Kommentare sind möglich aber nicht nötig).
Bei einem nicht zusammenhängenden Graphen als eingabe wird ein Knoten n ohne Kanten ausgegeben
Die Adjazenzlisten werden sortiert nach Ausgangsknoten jeweils als eine Zeile angegeben. Die einzelenen Kanten innerhalb einer Adjazenzliste werden ebenfalls sortiert (nach Zielknoten) ausgegben.

# How to Test
run `python main.py <file>`