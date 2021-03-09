#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import inspect
import os
import subprocess
import sys
from datetime import datetime

# Find first .halex file
HALE_PROJECT = glob.glob('*.halex')[0]
# Use url from environment, or use default (prod)
WFS_URL = os.getenv('WFS_URL', 'https://stationsregister.miljodatasamverkan.se/geoserver/stationsregistret/wfs?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=stationsregistret:active_site')
# Export to different folder every time
OUTPUT_DIR = os.path.join('output', datetime.today().strftime(f'%Y%m%d%H%M%S'))

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def main(argv):
    datahosts = {
        '1': 'SE_EF_StnReg_DV_Sjoar_vattendrag',
        '2': 'SE_EF_StnReg_DV_Provfiske',
        '3': 'SE_EF_StnReg_DV_Grundvatten',
        '4': 'SE_EF_StnReg_DV_Oceanografi_marinbiologi',
        '6': 'SE_EF_StnReg_DV_Miljogifter',
        '7': 'SE_EF_StnReg_DV_Luftkvalitet',
        # '8' : 'SE_EF_StnReg_DV_Jordbruksmark',
        '10': 'SE_EF_StnReg_DV_Badvatten',
        '11': 'Stralningsmatningar_SSM',
        '12': 'SE_EF_StnReg_DV_Naturdata_faglar_fjarilar',
        # '?' : 'Nitrat_matstationer_JV',
        # '?' : 'SE_EF_StnReg_DV_Halsorelaterad_miljoovervakning',
    }

    for datahost_id, filename in datahosts.items():
        out_file = os.path.join(OUTPUT_DIR, f'{filename}.gml')
        out_report_file = os.path.join(OUTPUT_DIR, f'{filename}.log')

        subprocess.run([
            'hale',
            'transform',
            '-project', HALE_PROJECT,
            '-source', WFS_URL,
            '-filter', f"CQL:datahost_id = '{datahost_id}'",
            '-providerId', 'eu.esdihumboldt.hale.io.gml.reader',
            '-target', out_file,
            '-preset', 'InspireGML',
            '-reportsOut', out_report_file
        ])


if __name__ == '__main__':
    main(sys.argv[1:])
