#!/usr/bin/python3
# 
# stnreg2gml.py
# extraherar data från StnReg och skapar Inspire GML filer
# för varje datavärdskap och för hela StnReg
# 
# behöver python3 och HALE Studio
# 
# Usage:
# python3 stnreg2gml.py
#
# version 0.5
# 2024-10-30
# 
# Hernán De Angelis, GeoNatura AB / HaV

import sys
import os
from datetime import date
from datetime import datetime as DT

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# grundparametrarna, anpassa vid behov

# HALE körbar fil
HALEexecutable = "/usr/local/hale-studio-5.3.0-linux.gtk.x86_64/HALE"

# HALE Inspire mappning
HALEprojekt = "SE_EF_StnReg_Stationsregistret.halex"

# StnReg WFS anrop, inlusive tabell
StnRegWFS = "https://stationsregister.miljodatasamverkan.se/geoserver/stationsregistret/wfs?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&TYPENAME=stationsregistret:active_site"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# datavärdskapskoder och filnamn

# dessa ändras enbart i fall av ändringar i registret
datavarsdsKoder = {
'3' : 'Platser för miljöövervakning: Datavärdskap Grundvatten',
'7' : 'Platser för miljöövervakning: Datavärdskap Luftkvalitet',
'12' : 'Platser för miljöövervakning: Datavärdskap Naturdata fåglar och fjärilar',
'10' : 'Platser för miljöövervakning: Datavärdskap Badvatten',
'11' : 'Platser för miljöövervakning: Strålningsmätningar (SSM)',
'1' : 'Platser för miljöövervakning: Datavärdskap Sjöar och vattendrag',
'4' : 'Platser för miljöövervakning: Datavärdskap Oceanografi och marinbiologi',
'2' : 'Platser för miljöövervakning: Datavärdskap Provfiske',
'6' : 'Platser för miljöövervakning: Datavärdskap Miljögifter',
# 	'8' : 'Platser för miljöövervakning: Datavärdskap Jordbruksmark',
# 	'9' : 'Platser för miljöövervakning: Datavärdskap Hälsorelaterad miljöövervakning',
}

# dessa ändras enbart i fall av ändringar i filbenämningskonventionen
gmlFilNamn = {
'3' : 'SE_EF_StnReg_DV_Grundvatten',
'7' : 'SE_EF_StnReg_DV_Luftkvalitet',
'12' : 'SE_EF_StnReg_DV_Naturdata_faglar_fjarilar',
'10' : 'SE_EF_StnReg_DV_Badvatten',
'11' : 'SE_EF_StnReg_Stralningsmatningar',
'1' : 'SE_EF_StnReg_DV_Sjoar_vattendrag',
'4' : 'SE_EF_StnReg_DV_Oceanografi_marinbiologi',
'2' : 'SE_EF_StnReg_DV_Provfiske',
'6' : 'SE_EF_StnReg_DV_Miljogifter',
# 	'8' : 'SE_EF_StnReg_DV_Jordbruksmark',
# 	'9' : 'SE_EF_StnReg_DV_Halsorelaterad_miljoovervakning',
}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# skappa logfil

# få dagens datum
idag = date.today()

loggFilNamn = f"""StnReg2gml_{idag}.log"""
file = open(loggFilNamn,"w")
file.close()

# funktion för att skriva ut logmeddelande med tidstämpel
def writeLog(loggMeddelande):
    "skriv tidsstämpel och logg meddelande till stdout och loggfilen"
    # få tidsStampel
    tidsStampel = DT.today()        
    # skriv till stdout
    print()
    print(f"{tidsStampel}: {loggMeddelande}")
    # skriv ut till loggfil
    file = open(loggFilNamn,"a")
    file.write(f"{tidsStampel}: {loggMeddelande}\n")
    file.close()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# skapa Inspire GML

# gå igenom varje datavärdskap
for datavarsdsKod in datavarsdsKoder:
    writeLog(f"""{datavarsdsKoder[datavarsdsKod]}: startar""")
    
    # # vid behov, skriv ut kommando till stdout för kontroll
    # print(f"""{HALEexecutable} -nosplash -application hale.transform -project "{HALEprojekt}" -source "{StnRegWFS}" -filter "CQL:datahost_id = '{datavarsdsKod}'" -providerId eu.esdihumboldt.hale.io.gml.reader -target "{gmlFilNamn[datavarsdsKod]}.gml" -preset InspireGML -reportsOut "report.log" """)
    
    # kör HALE transformering
    os.system(f"""{HALEexecutable} -nosplash -application hale.transform -project "{HALEprojekt}" -source "{StnRegWFS}" -filter "CQL:datahost_id = '{datavarsdsKod}'" -providerId eu.esdihumboldt.hale.io.gml.reader -target "{gmlFilNamn[datavarsdsKod]}.gml" -preset InspireGML -trustGroovy -reportsOut "report.log" """)
    writeLog(f"""{datavarsdsKoder[datavarsdsKod]}: klart\n""")
    
    # komprimera filerna
    os.system(f"""zip {gmlFilNamn[datavarsdsKod]}.zip {gmlFilNamn[datavarsdsKod]}.gml""")
        

# harmonisera hela StnReg
writeLog(f"""Hela StnReg: startar""")

# kör HALE transformering
os.system(f"""{HALEexecutable} -nosplash -application hale.transform -project "{HALEprojekt}" -source "{StnRegWFS}" -providerId eu.esdihumboldt.hale.io.gml.reader -target "SE_EF_StnReg.gml" -preset InspireGML -trustGroovy -reportsOut "report.log" """)
writeLog(f"""Hela StnReg: klart\n""")

# komprimera filerna
os.system(f"""zip SE_EF_StnReg.zip SE_EF_StnReg.gml""")    

