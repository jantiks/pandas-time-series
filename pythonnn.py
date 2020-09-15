import pandas_datareader.data as web
import datetime
start = datetime.datetime(2018,1,1)
end = datetime.datetime(2020,1,1)
BTC = web.DataReader("FB","yahoo",start,end)
print(BTC.head())
import quandl
import matplotlib.pyplot as plt
btc = quandl.get("WIKI/AAPl.1")
btc.plot()
plt.show()