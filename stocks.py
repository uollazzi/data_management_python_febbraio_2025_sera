import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import os


def load_data(ticker, start_date, end_date):
    t = yf.Ticker(ticker)

    file_path = os.path.join("data", ticker + ".csv")

    df = pd.DataFrame()

    if not os.path.exists(file_path):
        df = t.history(start=start_date, end=end_date, interval="1d")
        df.to_csv(file_path)
        print(f"Dati {ticker} scaricati con successo da Yahoo Finance.")
    else:
        df = pd.read_csv(file_path, index_col="Date", parse_dates=["Date"])
        print(f"Dati {ticker} caricati da file.")

    return df


start_date = "2024-01-01"
end_date = "2024-12-31"

dfBMW = load_data("1BMW.MI", start_date, end_date)
dfMercedes = load_data("1MBG.MI", start_date, end_date)

plt.figure(figsize=(10, 5))
sns.lineplot(x=dfBMW.index, y=dfBMW["Close"], label="BMW")
sns.lineplot(x=dfMercedes.index, y=dfMercedes["Close"] * 1.7, label="Mercedes")
plt.xlabel("Data")
plt.ylabel("Prezzo")
plt.title("Prezzi di chiusura")
plt.legend()
plt.show()
# plt.savefig("chart.png")
