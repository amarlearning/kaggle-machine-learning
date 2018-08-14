## 1. Reading CSV files with NumPy ##

import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header = 1)

## 2. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100

## 3. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

# for January month
january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

# for Feburary month
february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

# for March month
march_bool = pickup_month == 3
march = pickup_month[march_bool]
march_rides = march.shape[0]