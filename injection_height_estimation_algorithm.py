"""
Injection height estimation algorithm
-------------------------------------
Generates a .mat file with the 
- smoke injection heights for each grid square
- times that radar data is retrieved
- maximum injection heights at each time stamp
- latitude positions of each grid square
- longitude positions of each grid square
"""

# Importing relevat packages
import os
import numpy as np
import pandas as pd
import scipy.io as sio
import pyart

# =============================================
# HELPER FUNCTION
# function to convert time string to seconds
def convert_time(timestr):
    hourstr = timestr[0] + timestr[1]
    minstr = timestr[2] + timestr[3]
    secstr = timestr[4] + timestr[5]
    
    hours = float(hourstr)*3600
    mins = float(minstr)*60
    secs = float(secstr)
    
    totals = hours + mins + secs
    
    return totals
# =============================================

# Reading in all radar files
# each radar file corresponds to the radar data
# retrieved at a specific time stamp
# =============================================
# change these following as required before running script
date_num = 2 # change the day as needed. Here, the day = 2 Aug 2019
path = ".../data_2-Aug-2019/" # change the path as required
# =============================================
# appending all filenames to a list, in temporal order
filenames = []
for root, dirs, files in os.walk(path):
    for f in sorted(files):
        for i in range(10):
            if f.startswith('KOTX2019080'+str(date_num)+'_0'+str(i)):
                filenames.append(f)
        for j in range(10, 24):
            if f.startswith('KOTX2019080'+str(date_num)+'_'+str(i)):
                filenames.append(f)

# Empty lists to store data
injection_heights = []
x_coordinates = []
y_coordinates = []
df = pd.DataFrame() # empty data frame

# Decide the bounds for the pre-determined grid
# =============================================
# define the pre-determined grid for the fire
lower_latitude = 47.85
upper_latitude = 48.05
lower_longitude = -118.70
upper_longitude = -118.30
# =============================================
# reading in a single file
file = filenames[0]
# creating a radar object with PyART
radar = pyart.io.read(path+file)
# re-gridding the radar data with PyART, creating a PyART grid object
# we can use the 'grid' object to access radar data values
grid = pyart.map.grid_from_radars((radar,), grid_shape=(100,200,200),
                                     grid_limits=((0,10000), (-125000.0, 125000.0), (-125000.0, 125000.0)))
# initializing the (x, y) bounds of the p=pre-determined grid
xmin = grid.nx 
ymin = grid.ny
xmax = 0
ymax = 0

for x in range(grid.nx):
    for y in range(grid.ny):
        # current latitude and longitude
        lat = grid.point_latitude['data'][0, y, x]
        long = grid.point_longitude['data'][0, y, x]

        # finding the bounds of the pre-determined grid
        # bottom boundary of pre-determined grid
        if lat >= lower_latitude:
            if y < ymin:
                ymin = y
        # upper boundary of pre-determined grid
        if lat <= upper_latitude:
            if y > ymax: 
                ymax = y
        # left boundary of pre-determined grid
        if long >= lower_longitude:
            if x < xmin: 
                xmin = x
        # right boundary of pre-determined grid
        if long <= upper_longitude:
            if x > xmax:
                xmax = x
# pre-determine grid, results
print('Pre-determined grid: xmin = ', xmin, 'ymin = ', ymin, 'xmax = ', xmax, 'ymax = ', ymax)

xlen = (xmax+1)-xmin
ylen = (ymax+1)-ymin
tlen = len(filenames)

# Injection height estimation algorithm
# -------------------------------------
all_heights = np.zeros(xlen*ylen*tlen).reshape(xlen, ylen, tlen) # all smoke heights for each grid square

file_number = 0 # file number
for file in filenames:
    print('Reading file = ', file_number, '------ files remaining = ', len(filenames)-(file_number+1))

    # creating a PyART radar object
    radar = pyart.io.read(path+file)
    # converting data to cartesian grid, PyART grid object
    grid = pyart.map.grid_from_radars((radar,), grid_shape=(100,200,200),
                                     grid_limits=((0,10000), (-125000.0, 125000.0), (-125000.0, 125000.0)))
    
    # maximum injection heights for this radar file, for each grid square
    max_altitudes = np.zeros(xlen*ylen).reshape(xlen, ylen)

    # arrays tp store (x, y) positions and altitude
    altitudes = np.array([])
    x_points = np.array([])
    y_points = np.array([])

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):

            current_height = -1
            bad_count = 0 # bad value counter

            for z in range(grid.nz):

                # reflectivity and correlation coefficient
                ref_type = str(type(grid.fields['reflectivity']['data'][z][y][x]))
                coeff_type = str(type(grid.fields['cross_correlation_ratio']['data'][z][y][x]))

                if ref_type=="<class 'numpy.float32'>" and coeff_type=="<class 'numpy.float32'>":
                    ref = float(grid.fields['reflectivity']['data'][z][y][x])
                    coef = float(grid.fields['cross_correlation_ratio']['data'][z][y][x])

                    # adjust the thresholds of reflectivity and correlation coefficent
                    # as required
                    if ref >= 10.000 and coef > 0.2 and coef < 0.9:
                        current_height = grid.point_altitude['data'][z][y][x]
                    else:
                        bad_count += 1
                else:
                    bad_count += 1

                # returning the maximum injection height if the 
                # number of 'bad' values > 2
                if bad_count > 2:
                    max_altitudes[x-xmin][y-ymin] = current_height
                    altitudes = np.append(altitudes, current_height)
                    x_points = np.append(x_points, x)
                    y_points = np.append(y_points, y)
                    break 
    
    # injection height
    max_altitude = np.max(altitudes)
    x_pos = x_points[np.argmax(altitudes)]
    y_pos = y_points[np.argmax(altitudes)]

    all_heights[:,:,file_number] = max_altitudes
    file_number += 1
    injection_heights = np.append(injection_heights, max_altitude)
    x_coordinates.append(x_pos)
    y_coordinates.append(y_pos)

# Grabbing latitude-longitude values for the 
# pre-determined grid
print('grabbing the latitudes and longitudes...')
latitudes = np.zeros(xlen*ylen).reshape(xlen, ylen)
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        current_lat = grid.point_latitude['data'][0][y][x]
        latitudes[x-xmin][y-ymin] = current_lat
        
longitudes = np.zeros(xlen*ylen).reshape(xlen, ylen)
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        current_long = grid.point_longitude['data'][0][y][x]
        longitudes[x-xmin][y-ymin] = current_long

# Grabbing the times for all of the radar files
print('grabbing the times...')
times = np.zeros(len(filenames))
for i, file in enumerate(filenames):
    time = convert_time(file.split("_")[1])
    times[i] = time

# Saving the results
print('saving the results...')
# dictionary of results
savedict = {
    'smoke_injection_height' : all_heights,
    'time' : times,
    'max_injection_height' : injection_heights,
    'latitudes' : latitudes,
    'longitudes' : longitudes,
}
# ======================================================
# change the file name accordingly
save_file_name = 'new-injection-heights_'+str(date_num)+'-Aug-2019.mat'
# ======================================================
sio.savemat(save_file_name, savedict)

    












