#! /bin/bash

python3 /hd1/fer/Documents/SWPeru/swperu_bloco/goes_flux7days.py
python3 /hd1/fer/Documents/SWPeru/swperu_bloco/goes_proton7days.py
python3 /hd1/fer/Documents/SWPeru/swperu_bloco/solar_cycle_index.py
python3 /hd1/fer/Documents/SWPeru/swperu_bloco/solar-wind_realtime.py
cd /media/hd2/GitHub/vlslv.github.io
git commit -am "actualizando" && git push origin main
