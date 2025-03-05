import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

start_date = "2024-01-01"
end_date = "2024-12-31"

bmw = yf.Ticker("1BMW.MI")
mercedes = yf.Ticker("1MBG.MI")

dfBMW = bmw.history(start=start_date, end=end_date, interval="1d")
dfMercedes = mercedes.history(start=start_date, end=end_date, interval="1d")

dfBMW.to_csv("data/1BMW.csv")

# dfBMW.index = pd.to_datetime(dfBMW.index)

plt.figure(figsize=(10, 5))
sns.lineplot(x=dfBMW.index, y=dfBMW["Close"], label="BMW")
sns.lineplot(x=dfMercedes.index, y=dfMercedes["Close"] * 1.7, label="Mercedes")
plt.xlabel("Data")
plt.ylabel("Quantità")
plt.title("Quantità vendute nel tempo")
plt.legend()
plt.show()
# plt.savefig("chart.png")
