#created Feb 03, 2024 >>>> KFLA - Br

import pandas as pd
import matplotlib.pyplot as pl
from matplotlib.dates import DateFormatter
import datetime as dt
import numpy as np
from astropy.visualization import time_support
from sunpy import timeseries as ts
from sunpy.net import Fido
from sunpy.net import attrs as a
import matplotlib.dates
from datetime import datetime
from datetime import timedelta
import datetime
from astropy.time import Time
import matplotlib.dates as mdates
from datetime import date

from sunpy.time import parse_time
from collections import OrderedDict
from astropy import units as u
import math

data = pd.read_json("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json").fillna(value=0)

dataB = pd.read_json("https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json").fillna(value=0)#, dtype={"None": 0})

time_array = parse_time(data[0][1:])
Density = [float((data[1][1:].values)[i]) for i in range(len(data[1][1:].values))]
Speed = [float((data[2][1:].values)[i]) for i in range(len(data[2][1:].values))]
Temperature = [float((data[3][1:].values)[i]) for i in range(len(data[3][1:].values))]
Temperature = [np.mean(Temperature) if x<=0 else x for x in Temperature];

#*********Magnetic field************
timeB_array = parse_time(dataB[0][1:])

Bx = [float((dataB[1][1:].values)[i]) for i in range(len(dataB[1][1:].values))]
By = [float((dataB[2][1:].values)[i]) for i in range(len(dataB[2][1:].values))]
Bz = [float((dataB[3][1:].values)[i]) for i in range(len(dataB[3][1:].values))]
Bt = [float((dataB[6][1:].values)[i]) for i in range(len(dataB[6][1:].values))]
Lat = [float((dataB[5][1:].values)[i]) for i in range(len(dataB[5][1:].values))]
Lon = [float((dataB[4][1:].values)[i]) for i in range(len(dataB[4][1:].values))]

#Lat
#Bt

#------------------Plot------------------------------
fig,(ax, ax2, ax3, ax4) = pl.subplots(4, 1, figsize = (8.5,7.5)) #(x,y)
#fig.subplots_adjust(bottom=1.9, right=2.0, top=3.8,wspace=0.5)
fig.tight_layout(pad=2)
#**********Bx,By,Bz***************
#ax0.axhspan(np.min(Bz),0,color='gray',alpha = 0.4,lw=0)
#ax0.axhspan(0,np.max(Bz),color='yellow',alpha=0.4,lw=0)

#ax0.scatter(timeB_array.datetime,Bx,color ='crimson',alpha =0.5,sizes=[1], label= '$B_x$')
#ax0.scatter(timeB_array.datetime,By,color ='darkgreen',alpha =0.5,sizes=[1], label= '$B_y$')
#ax0.scatter(timeB_array.datetime,Bz,color ='deepskyblue',alpha =0.5,sizes=[0.9], label= '$B_z$')
# ax.set_yscale("log")
#ax0.grid(linestyle='dotted')
#ax0.set_ylim(np.min(Bz),np.max(Bz))
#ax0.set_ylabel('Componentes B $[nT]$')
ax.set_title('Satélite ACE: Detector de viento solar (SWEPAM) y Magnetómetro',fontweight="bold")
ax.set_title('ACE Satellite - Solar Wind Electron Proton Alpha Monitor (SWEPAM) & Magnetometer',fontweight="bold")

#*********Bt******************

ax.axhspan(0,np.max(Bt),color='gray',alpha = 0.2,lw=0)
ax.scatter(timeB_array.datetime,Bt,color ='black',sizes=[0.2], label= 'Bt $[nT]$')#,alpha =0.3
#ax0.set_yscale("log")
ax.grid(linestyle='dotted')
ax.set_ylabel('|Bt| $[nT]$')
ax.set_ylim(0,np.max(Bt))
#********Long************

# ax1.axhspan(1e-1,1e0,color='gray',alpha = 0.2,lw=0)
# ax1.axhspan(1e0,1e1,color='yellow',alpha=0.5,lw=0)
# ax1.axhspan(1e1,np.max(Density),color='red',alpha=0.5,lw=0)
#ax1.axhspan(1e-1,370,color='gray',alpha = 0.4,lw=0)
#ax1.scatter(timeB_array.datetime,Lon,color ='purple',alpha =0.2,sizes=[0.2])
# ax1.set_yscale("log")
#ax1.grid(linestyle='dotted')
#ax1.set_ylabel('Longitud ($⁰$)')
#ax1.set_ylim(1e-1,370)

#*******Density*********
#1e-1
ax2.axhspan(np.min(Density),1e0,color='gray',alpha = 0.4,lw=0)
ax2.axhspan(1e0,1e1,color='yellow',alpha=0.4,lw=0)
ax2.axhspan(1e1,np.max(Density),color='orange',alpha=0.4,lw=0)

ax2.scatter(time_array.datetime,Density,color ='green',alpha =0.3,sizes=[0.2])
ax2.set_yscale("log")
ax2.grid(linestyle='dotted')
ax2.set_ylabel('Densidad $[cm^{-3}]$')
ax2.set_ylim(1e-1,np.max(Density))

#*******Speed*************
# ax3.axhspan(1e-1,1e0,color='gray',alpha = 0.2,lw=0)
# ax3.axhspan(1e0,np.max(Density),color='yellow',alpha=0.5,lw=0)
ax3.axhspan(np.min(Speed),np.max(Speed),color='gray',alpha = 0.4,lw=0)
ax3.scatter(time_array.datetime,Speed,color ='red',alpha =0.4,sizes=[0.2]) #,marker= '.'
ax3.grid(linestyle='dotted')
ax3.set_ylabel('Velocidad $[km\cdot s^{-1}]$')
#ax3.set_ylim(1e-1,450)
ax3.set_ylim(np.min(Speed),np.max(Speed))

#*******Temperature*************
ax4.axhspan(np.min(Temperature),1e5,color='gray',alpha = 0.4,lw=0)
ax4.axhspan(1e5,np.max(Temperature),color='yellow',alpha=0.4,lw=0)

ax4.scatter(time_array.datetime,Temperature,color ='blue',alpha =0.4,sizes=[0.2])
ax4.grid(linestyle='dotted')
ax4.set_ylabel('Temperatura $[K]$')
ax4.set_yscale("log")
ax4.set_ylim(np.min(Temperature),np.max(Temperature))


ax4.set_xlabel('Año-Mes-Día')

#ax0.legend(loc=1)
#ax1.legend(loc=1)
# ax2.legend(loc=2)

pl.savefig('/media/hd2/GitHub/vlslv.github.io/all_data/solarwind_Tmag_plasma7days_ACE.jpg',dpi=600)

