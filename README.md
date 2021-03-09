# stnreg2gml
Konvertera Stationsregistret till Inspire GML

## Om

Skriptet skapar Inspire GML filer för varje datavärdskap och för hela Stationsregistret. 

Uttag görs ur databasen genom WFS tjänsten, tabellen "active_site". Skriptet anropar sedan [hale-cli](https://github.com/halestudio/hale-cli) och passar argument för att harmonisera olika datavärdskap och hela Stationsregistret. 


## Användning

Kör script:
`docker-compose up` - Filerna hittas i `output`

Kör script efter du modifierat någon fil:
`docker-compose up --build`

Hale exporterar från `https://stationsregister.miljodatasamverkan.se` men kan modifieras genom att skicka med miljövariabel `WFS_URL` i `docker-compose.yml`. Ex
```
environment:
  - WFS_URL=https://stationsregistertest.miljodatasamverkan.se/geoserver/stationsregistret/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=stationsregistret:active_site
```

## Filer

`stnreg2gml.py` : själva skriptet

`SE_EF_StnReg_Stationsregistret.halex`: HALE projekt

`SE_EF_StnReg_Stationsregistret.halex.alignment.xml`: mappningen

`SE_EF_StnReg_Stationsregistret.halex.styles.sld`: (tom) SLD fil, en del av HALE projektet

## Begränsningar

Skriptet skapar i nuläge inte GML för Nitrat_matstationer_JV. Dessa behöver än så länge exporteras manuellt.
