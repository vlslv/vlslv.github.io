## Created:     Thu 04 Jan 2024 10:01:53 PM JST (DPC)
## Modified:    Fri 16 Feb 2024 11:50:05 PM JST (DPC)
## Comments:
"""
    A script to retrieve and plot solar-cycle index, and NOAA prediction of sunspot number.

    Project: SWP
"""

import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
import datetime
"""
import astropy.units as u
from astropy.time import Time, TimeDelta
from astropy.visualization import time_support

import sunpy.timeseries as ts
from sunpy.net import Fido
from sunpy.net import attrs as a
from sunpy.time import TimeRange

time_range = TimeRange("2008-06-01 00:00", Time.now())
result = Fido.search(a.Time(time_range), a.Instrument('noaa-indices'))
f_noaa_indices = Fido.fetch(result)
noaa = ts.TimeSeries(f_noaa_indices, source='noaaindices').truncate(time_range)

time_support()
fig = pl.figure(1, figsize=[12.5, 4.5])
ax = fig.add_axes( (0.07, 0.1, 0.90, 0.86) )
ax.plot(noaa.time, noaa.quantity('sunspot RI'), label='Sunspot Number')  ## error happens here because empty data!!
"""

data = pd.read_json("https://services.swpc.noaa.gov/json/solar-cycle/observed-solar-cycle-indices.json")

model = pd.read_json("https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json")


year_month_obs = pd.to_datetime(data['time-tag'])
sn_index_obs = data["ssn"]
year_month_mod = pd.to_datetime(model['time-tag'])
sn_index_mod = model["predicted_ssn"]

fig = pl.figure(1, figsize=[8.5, 4.5])
ax = fig.add_axes( (0.07, 0.15, 0.90, 0.82) )
ax.plot_date(year_month_obs, sn_index_obs, 'k.-', label='$Observaci\\acute{o}n$', lw=0.9)
ax.plot_date(year_month_mod, sn_index_mod, '-', color='crimson', label='$Predicci\\acute{o}n~NOAA$', lw=1.0)
ax.fill_between(year_month_mod, model["low_ssn"], model["high_ssn"], alpha=0.3, color='crimson')
#    noaa_predict.time, noaa_predict.quantity('sunspot low'),
#    noaa_predict.quantity('sunspot high'), alpha=0.3, color='grey'

ax.legend()
#ax.set_xlim('1996-01-01 00:00:00', '2035-01-01 00:00:00')
ax.set_xlim(datetime.date(1996,1,1),datetime.date(2035,1,1))
ax.set_ylim(0, 250)
#ax.plot([2020,2020], [0, 250], 'b--')
ax.set_ylabel('${\\rm N\\acute{u}mero~de~manchas~solares~(SSN)}$')
ax.set_xlabel('${\\rm A\~no}$')
ax.grid(linestyle='dotted')
pl.gcf().autofmt_xdate()
#pl.show()

pl.savefig('/media/hd2/GitHub/vlslv.github.io/all_data/swpc_sunspotcycle.jpg', dpi=255)
