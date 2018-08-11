## 1. Introduction ##

import csv

def read_data(fileame):
    f = open(fileame, "r")
    return list(csv.reader(f))

music = read_data("global_rankings.csv")

## 2. Using the datetime module ##

from datetime import datetime

jan_27_1965 = datetime(1965, 1, 27, 12, 43)
aug_3_1972 = datetime(1972, 8, 3, 1, 43)
oct_31_2000 = datetime(2000, 10, 31, 15, 12)
mar_2_2017 = datetime(2017, 3, 2, 7, 30)

## 3. Creating a datetime object using a string ##

date_jun_2_08 = "6-02-2008"
date_jul_15_01 = "7?15?2001"
date_dec_20_08 = "12--30--2010"

jun_2_08 = datetime.strptime(date_jun_2_08, "%m-%d-%Y")
jul_15_01 = datetime.strptime(date_jul_15_01, "%m?%d?%Y")
dec_20_08 = datetime.strptime(date_dec_20_08, "%m--%d--%Y")
