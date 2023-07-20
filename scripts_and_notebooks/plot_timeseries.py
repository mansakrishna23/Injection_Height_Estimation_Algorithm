"""
Plotting a time series of injection heights 
-------------------------------------
This file contains code for plotting a time series of heights
for one day as well as an extended time series (currently commented out)

Comment out the part of the code, according to which plot you want
"""

# Importing relevant packages
import os
import numpy as np
import pandas as pd
import scipy.io as sio
import pyart
import matplotlib.pyplot as plt

# Plotting the results for one day
# =================================================================================
filename = 'new-injection-heights_2-Aug-2019.mat' # change the file name accordingly
results = sio.loadmat(filename)

# retrieving the injection heights and times
heights = results['smoke_injection_height'].max(axis=0).max(axis=0)
times = results['time'][0]/3600 # convert from seconds to hours
# removing all negative values
for n in range(len(times)):
    if heights[n] < 0:
        heights[n] = np.NaN

# Plotting the results 
# All of the parameters may be customized
plt.figure(figsize=(15, 10))
plt.grid()
plt.plot(times, heights, marker='x', label=r"Ref $\geq$ 10 dBZ, Coef 0.2 < C.C. < 0.9")
plt.legend(loc='best')
plt.title('2 August 2019 Injection Heights', fontsize=18)
plt.xlabel("Time [hours] after 00:00 UTC", fontsize=14)
plt.ylabel("Injection Height [meters above sea level]", fontsize=14)
# For PST time, limit the axis [7, 25]
# plt.xlim(7, 25)
plt.show()

# save the figure if satisfied with the same
# plt.savefig('new-injection-heights_2-Aug-2019.png')

# Plotting the results for many days
# =================================================================================
# =====================================
path = '../Injection-Heights/' # change the path as needed
# change the start, end days as needed
start_day = 2
end_day = 9
# find the unixtimes for the days you want (2-8 Aug 2019)
unixtimes = [1564704000, 1564790400, 1564876800, 1564963200, 1565049600, 1565136000, 1565222400]
# =====================================

# Array of times and heights
all_heights = np.array([])
all_times = np.array([], dtype=np.datetime64)

# looping through the days 
for day in range(start_day, end_day):
    # reading in the current results file
    current_day = sio.loadmat(path+"new-injection-heights_"+str(day)+"-Aug-2019.mat")
    current_times = np.array(current_day['time'][0]) # times for current day

    unixtime = unixtimes[day-start_day] # retrieving the unixtime for the current day
    tdelta = np.full(len(current_times), unixtime)
    # re-writing times, from seconds to np.datetime
    times = current_times + tdelta
    times = np.array(times, dtype='datetime64[s]')

    # retrieve maximum heights
    for t in range(len(current_times)):
        max_height = np.max(current_day['smoke_injection_height'][:, :, t])
        all_times = np.append(all_times, times[t])
        if max_height < 0:
            all_heights = np.append(all_heights, np.NaN)
        else:
            all_heights = np.append(all_heights, max_height)

# Plotting the extended time series
# ----------------------------------
# parameters can be customized accordingly
plt.figure(figsize=(20, 10))
plt.plot(all_times, all_heights, label=r"Ref $\geq$ 10 dBZ, 0.2 < C.C < 0.9")
plt.title("Time Series of Injection Heights, 2-9 August 2019 UTC", fontsize=23)
plt.grid()
plt.ylabel('Injection Height [meters above sea level]', fontsize=20)
plt.xlabel('Time (UTC)', fontsize=20)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.legend(fontsize=13)
plt.show()

# Uncomment this when you are satisfied with the result
# Change the file name as required
# plt.savefig("timeseries.png")