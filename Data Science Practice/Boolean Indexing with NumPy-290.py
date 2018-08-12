## 1. Reading CSV files with NumPy ##

import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header = 1)