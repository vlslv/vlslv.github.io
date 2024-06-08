## Creadted:    Sat 25 Nov 2023 12:06:30 AM JST (DPC)
## Modified:    Fri 23 Feb 2024 03:13:25 PM JST   (DPC)
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
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

hours = mdates.HourLocator([0,6,12,18,24])##interval = 6)
h_fmt = mdates.DateFormatter('%H')

data = pd.read_json("https://services.swpc.noaa.gov/json/goes/secondary/xrays-7-day.json")
sxr_short = data[data["energy"]=="0.05-0.4nm"]
sxr_long  = data[data["energy"]=="0.1-0.8nm"]
time_array = parse_time(sxr_short["time_tag"])

fig = pl.figure(1, figsize=[12.5, 4.5])
ax1 = fig.add_axes( (0.07, 0.12, 0.90, 0.86) )
ax1.spines[['left', 'right', 'top']].set_visible
#ax1.yaxis.set_major_locator(ticker.NullLocator())
ax1.tick_params(which='major', width=1.00, length=5)
ax1.tick_params(which='minor', width=0.75, length=2.5, direction="in", pad=-10, labelsize=8)

ax1.plot(time_array.datetime, sxr_long['flux'].values, 'k', label='1.0-0.8 $\AA$')
ax1.plot(time_array.datetime, sxr_short['flux'].values, c='dodgerblue', label='0.5-4.0 $\AA$')
ax1.set_yscale('log')
ax1.set_xlim(left=time_array.datetime[0])
ax1.set_ylim(1.e-8, 1.e-2)
ax1.set_ylabel('Flujo de rayos-X blandos ($Watts/m^2$)')
ax1.set_xlabel('$({\\rm A\~no-Mes-D\\acute{i}a})$')
ax1.grid(which='major', linestyle='dotted')
ax1.grid(which='minor', linestyle='dotted',markersize=0.5)
ax1.legend()
ax1.axhspan(1.e-8, 1.e-6, color='gray', alpha=0.2, lw=0)
ax1.axhspan(1.e-6, 1.e-5, color='yellow', alpha=0.6, lw=0)
ax1.axhspan(1.e-5, 1.e-4, color='orange', alpha=0.7, lw=0)
ax1.axhspan(1.e-4, 1.e-2, color='red', alpha=0.8, lw=0)
ax1.xaxis.set_minor_locator(hours)
ax1.xaxis.set_minor_formatter(h_fmt)

#pl.ioff()
#pl.show()
#pl.tight_layout()
pl.savefig('/media/hd2/GitHub/vlslv.github.io/all_data/goes_flux7days_latest.jpg', dpi=180)
