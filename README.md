# stnreg2gml
Harmonisera Stationsregistret till Inspire GML

## Om

Skriptet skapar Inspire GML filer för varje datavärdskap och för hela Stationsregistret. 

Uttag görs ur databasen genom WFS tjänsten, tabellen "active_site". Skriptet anropar sedan [HALE Studio](https://github.com/halestudio/hale) och passar argument för att harmonisera olika datavärdskap och hela Stationsregistret. 


## Användning

`python3 stnreg2gml.py`

eller, om man gör filen körbar:

`stnreg2gml.py`



## Filer

`stnreg2gml.py` : själva skriptet

`SE_EF_StnReg_Stationsregistret.halex`: HALE projekt

`SE_EF_StnReg_Stationsregistret.halex.alignment.xml`: mappningen

`SE_EF_StnReg_Stationsregistret.halex.styles.sld`: (tom) SLD fil, en del av HALE projektet


Alla filer behöver inte finnas i samma mapp, men det rekommenderas. Om filerna inte ska finnas i samma mapp ska sökvägen anges i skriptet.

Skriptet behöver också veta sökvägen till HALE körbarfilen, detta ska sättas i variabeln "HALEexecutable" i början.



## Förutsättningar

Skriptet är testat i Python-3.11.10, men det ska fungera väl i alla moderna Python med version > 3.8. Python modulerna `sys`, `os` och `datetime` ska vara tillgängliga.

Harmoniseringen kördes och testades i [HALE Studio](https://github.com/halestudio/hale) v 5.3.0, menska fungera väl i alla hale med version > 5.0.0.
