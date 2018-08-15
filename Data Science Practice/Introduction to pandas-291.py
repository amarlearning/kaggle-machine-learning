## 1. Understanding pandas and NumPy ##

import pandas as pd
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

f500_type = type(f500)
f500_shape = f500.shape

## 2. Introducing DataFrames ##

f500_head = f500.head(6)
f500_tail = f500.tail(8)
f500.info()

## 3. Selecting Columns From a DataFrame by Label ##

industries = f500.loc[:, "industry"]

previous = f500.loc[:, ["rank", "previous_rank", "years_on_global_500_list"]]

financial_data = f500.loc[:, "revenues" : "profit_change"]