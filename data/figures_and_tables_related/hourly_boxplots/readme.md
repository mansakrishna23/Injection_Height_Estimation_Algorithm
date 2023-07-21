### Hourly Boxplot Data
The data in the `.csv` file named `boxplot_data.csv` depicts an hourly comparison of injection heights between Doppler radar-derived injection heights and airborne lidar-derived injection heights. 

The data set includes the following:
- `Date (PST)`
- `Time (PST) [hours]`, the hour number. For an hour number `x`, all associated heights are retrieved between `(x-1):30:00` and `x:29:59`
- `R_max`, the radar-derived maximum height in meters (assumed to be the 90th percentile)
- `L_max`, the airborne lidar-derived maximum height in meters
- `R_mean`, the radar-derived mean height in meters
- `L_mean`, the airborne lidar-derived mean height in meters
- `R_median`, the radar-derived median height in meters
- `L_median`, the airborne lidar-derived median height in meters
- `R_iqr`, the interquartile range of the radar-derived heights in meters
- `L_iqr`, the interquartile range of the airborne lidar-derived heights in meters
