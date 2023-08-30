The files in this directory correspond to the retrieved results from Doppler Radar data using the injection height estimation algorithm (`detailed in injection_height_estimation.py`).

The `.mat` files contain the following information: 
- `smoke_injection_height` with dimension `nx x ny x nt` where `nx` and `ny` refer to the number of grid squares in the horizontal directions and `nt` refers to the number of time stamps.
- `time` with dimension `1 x nt`
- `max_injection_heights` with dimension `1 x nt`
- `latitudes` with dimension `nx x ny`
- `longitudes` with dimension `nx x ny`
