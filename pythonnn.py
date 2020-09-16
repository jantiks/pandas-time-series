import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# my_year = 2001
# my_month = 6
# my_day = 26
# my_hour = 18
# my_minute = 26
# my_second = 30
# my_date = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)
# print(my_date)
# df = pd.read_csv("walmart_stock.csv",index_col="Date",parse_dates=True)
# df["Date"] = pd.to_datetime(df["Date"])
# df.set_index("Date", inplace=True)

# print(df.resample("A").max())
df = pd.read_csv("walmart_stock.csv",index_col="Date",parse_dates=True)
df = df.shift(periods=-1)
print(df.tail())
