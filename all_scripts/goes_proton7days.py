## Creadted:    Sat 25 Nov 2023 12:06:30 AM JST (DPC)
## Modified:    Wed 21 Feb 2024 09:25:27 PM JST   (DPC)
## Comments:
""" A python script to download GOES soft-xray data and make a plot.
    Based on "goes_plot3days.py"

    Project: SWPERU
"""

import pandas as pd
from sunpy.time import parse_time
from sunpy import timeseries as ts
from collections import OrderedDict
from astropy import units as u
import matplotlib.pyplot as pl

data = pd.read_json("https://services.swpc.noaa.gov/json/goes/primary/integral-protons-7-day.json")
#data = pd.read_json('/Users/denis/pywork/script_test/Tasks/integral-protons-7-day.json')
flux_10MeV = data[data["energy"]==">=10 MeV"]
flux_50MeV = data[data["energy"]==">=50 MeV"]
flux_100MeV = data[data["energy"]==">=100 MeV"]
time_array = parse_time(flux_10MeV["time_tag"])

##pl.ion()
fig = pl.figure(1, figsize=[12.5, 4.5])
ax1 = fig.add_axes( (0.07, 0.12, 0.90, 0.86) )
#flux_ts = ts.TimeSeries(goes_data, meta, units, source="xrs")
#flux_ts.peek('Date: '+str(flux_ts.index[0])+' ~ '+str(flux_ts.index[-1]))

ax1.plot(time_array.datetime, flux_10MeV['flux'].values, 'r', label='$>= 10~MeV$')
ax1.plot(time_array.datetime, flux_50MeV['flux'].values, 'b', label='$>= 50~MeV$')
ax1.plot(time_array.datetime, flux_100MeV['flux'].values, 'g', label='$>= 100~MeV$')
ax1.set_yscale('log')
ax1.set_ylim(1.e-1, 1.e4)
ax1.set_ylabel('PFU $(Particulas \cdot cm^2 \cdot s^{-1} \cdot sr^{-1})$')
ax1.set_xlabel('$({\\rm A\~no-Mes-D\\acute{i}a})$')
ax1.grid(linestyle='dotted')
ax1.legend()
ax1.axhspan(1.e-1, 1.e1, color='gray', alpha=0.2, lw=0)
ax1.axhspan(1.e1, 1.e4, color='yellow', alpha=0.5, lw=0)

##pl.ioff()
#pl.show()
pl.savefig('/media/hd2/GitHub/vlslv.github.io/all_data/goes_proton7days_latest.jpg', dpi=255)
