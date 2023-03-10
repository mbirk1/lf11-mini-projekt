# Projektantrag

## Disclaimer  

## Beschreibung des Projekts

Das Projekt soll eine Anwendung sein, mit der es möglich ist seine Verkäufe und Käufe im Autionshaus
des MMORPGs World of Warcraft von Blizzard Activision zu festzuhalten. 

Die genannten Käufe und Verkäufe besitzen jeweils einen Preis, für den sie getätigt wurde, sowie eine
ID und ein zugehöriges Item, welches gehandelt wird. -> Preis in G/S/K 

-> Eine Auswertung passiert in der GUI.

## Genutzte Hilfsmittel

Als Hilfsmittel für die Entwicklung der Rest-Schnittstelle soll das Framework "FastAPI" genutzt werden.

-> Tkinter


## Erste Lösungsidee
Hierfür soll eine REST-
Schnittstelle implementiert werden, welche Http-Requests empfängt und auswertet. Nach der angegebenen
Auswertung soll eine Http-Response zurückgegeben werden.

Die Käufe und Verkäufe sollen den Vorgaben 
entsprechend in einer PostgreSQL Datenbank gespeichert werden, die in einem Docker-Container deployed 
wird.

-> MatPlot

-> Klare Trennung der Zuständigkeit
