# Projektantrag
  
## Beschreibung des Projekts

Das Projekt soll eine Anwendung sein, mit der es möglich ist seine Verkäufe und Käufe im Autionshaus
des MMORPGs World of Warcraft von Blizzard Activision zu festzuhalten. Hierfür soll eine REST-
Schnittstelle implementiert werden, welche Http-Requests empfängt und auswertet. Nach der angegebenen
Auswertung soll eine Http-Response zurückgegeben werden. 

Die genannten Käufe und Verkäufe besitzen jeweils einen Preis, für den sie getätigt wurde, sowie eine
ID und ein zugehöriges Item, welches gehandelt wird. Die Käufe und Verkäufe sollen den Vorgaben 
entsprechend in einer PostgreSQL Datenbank gespeichert werden, die in einem Docker-Container deployed 
wird.

## Genutzte Hilfsmittel

Als Hilfsmittel für die Entwicklung der Rest-Schnittstelle soll das Framework "FastAPI" genutzt werden.

## Erste Lösungsidee
