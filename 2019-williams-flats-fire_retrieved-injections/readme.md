### Injection Heights retrieved from WSR-88D dual polarization data
 
 The files within this folder are `.mat` files. The following information is stored. 
Let the pre-determined grid have size `(nx, ny)` and let the number of time stamps be `nt`. Each file contains: 
- `smoke_injection_height`, the injection height for each grid square within the pre-determined grid at every timestamp, with dimensions `(nx, ny, nt)`
- `time` the time in seconds for each retrieved height with dimensions `(1, nt)`
- `max_injection_heights` the maximum injection height at each timestamp with dimensions `(1, nt)`
- `latitudes` the latitudes for each grid square within the pre-determined grid, with dimensions `(nx, ny)`
- `longitudes` the longitudes for each grid square within the pre-determined grid, with dimensions `(nx, ny)`
