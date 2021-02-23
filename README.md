# stnreg2gml
Konvertera StnReg till Inspire GML

## Om

Skriptet skapar Inspire GML filer för varje datavärdskap och för hela Stationsregistret. 

Uttag görs ur databasen genom WFS tjänsten, tabellen "active_site". Skriptet anropar sedan HALE Studio och passar argument för att harmonisera olika datavärdskap och hela Stationsregistret. 


## Användning

python3 stnreg2gml.py

eller, om man gör filen körbar:

stnreg2gml.py 



## Filer

stnreg2gml.py: själva skriptet

SE_EF_StnReg_Stationsregistret.halex: HALE projekt

SE_EF_StnReg_Stationsregistret.halex.alignment.xml: mappningen

SE_EF_StnReg_Stationsregistret.halex.styles.sld: (tom) SLD fil, en del av HALE projektet


Alla filer behöver inte finnas i samma mapp, men det rekommenderas. Om filerna inte ska finnas i samma mapp ska sökvägen anges i skriptet.

Skriptet behöver också veta sökvägen till HALE körbarfilen, detta ska sättas i variabeln "HALEexecutable" i början.

Skriptet är skrivet och testat i Python-3.8.5, men det ska fungera väl i alla moderna Python >3.

Python moduler som behövs: sys, os, datetime


## Begränsningar
Skriptet skapar i nuläge inte GML för Nitrat_matstationer_JV. Dessa behöver än så länge exporteras manuellt.
