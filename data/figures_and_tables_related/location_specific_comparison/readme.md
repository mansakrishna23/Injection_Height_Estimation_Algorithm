### Location Specific Comparison Data
The `.mat` files for each of the days contain radar-specific data and radar-derived injection heights according to the flight-path of the airborne lidar (within the pre-determined grid around the fire). The `.csv` files provide an over-all summary of the `.mat` files. 

The `.mat` files contain the following data: 
- `reflectivity`: the vertical column of reflectivity retrieved at the position of the aircraft (with the airborne lidar), dimensions `(nt, nz)` where `nt` is the number of timestamps and `nz` is number of grid squares in the vertical direction.
- `correlation`: vertical column of correlation coefficients retrieved at the position of the aircraft (with the airborne lidar), dimensions `(nt, nz)`
- `altitudes`: the heights of each grid square in the vertical direction, dimensions `(nt, nz)`
- `latitudes`: the latitude positions of the retrieved radar data, closest to the aircraft position, dimensions `(1, nt)`
- `longitudes`: the longitude positions of the retrieved radar data, closest to the aircraft position, dimensions `(1, nt)`
- `injection_heights`: the radar-derived injection height at the specific latitude-longitude position, dimensions `(1, nt)`

The `.csv` files contain data about the radar and lidar derived injection heights in meters, the times of each of the injection height retrievals in hours, and the percentage difference between the two injection heights. 
