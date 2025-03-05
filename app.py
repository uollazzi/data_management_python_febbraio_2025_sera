import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_transactions = pd.read_csv(
    "data/sales_2022.csv", index_col="ID", parse_dates=["Date"]
)

# torna le prime n righe
print(df_transactions.head(3))

# torna le ultime n righe
print(df_transactions.tail())

# torna le dimensioni del df
print(df_transactions.shape)

# info varie
print(df_transactions.info())
# print(df_transactions.describe())

print(df_transactions["Date"].dtype)

# converte il tipo di dato
# df_transactions["Date"] = pd.to_datetime(df_transactions["Date"])

df_transactions["Date"] = df_transactions["Date"] + pd.DateOffset(years=-1)
# print(df_transactions["Date"])


# selezionare dati
print(df_transactions.loc["789671cb"]["Quantity"])  # seleziona in base a 1 indice
print(
    df_transactions.loc[["789671cb", "efea1d52"]]["Quantity"]
)  # seleziona in base a n indici (list)
print(
    df_transactions.loc["5f759728", "SalesPerson"]
)  # seleziona in base all'indice e alla colonna

df_transactions.loc["789671cb", "SalesPerson"] = 2

df_transactions.to_excel("data/sales_2021.xlsx")

# cercare per posizione
print(df_transactions.iloc[:5])

print(df_transactions[df_transactions["SalesPerson"] == 2])
print(df_transactions[df_transactions["Quantity"] > 3])

print(
    df_transactions[
        (df_transactions["Quantity"] >= 3) & (df_transactions["SalesPerson"] == 17)
    ]
)

plt.figure(figsize=(10, 5))
sns.lineplot(x=df_transactions["Date"], y=df_transactions["Quantity"])
plt.xlabel("Data")
plt.ylabel("Quantità")
plt.title("Quantità vendute nel tempo")
plt.legend()
# plt.show()
plt.savefig("chart.png")
