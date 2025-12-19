import pandas as pd
import os
import matplotlib.pyplot as plt

csv_folder = "C:/Stock_Analysis_Project/data_csv"

summary = []

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(csv_folder, file)

        df = pd.read_csv(file_path)

        # Calculate daily return
        df["daily_return"] = df["close"].pct_change()

        # Yearly return
        yearly_return = (df["close"].iloc[-1] - df["close"].iloc[0]) / df["close"].iloc[0]

        # Volatility
        volatility = df["daily_return"].std()

        summary.append({
            "Ticker": df["Ticker"].iloc[0],
            "Yearly_Return": yearly_return,
            "Volatility": volatility
        })

summary_df = pd.DataFrame(summary)

# Top gainers and losers
top_gainers = summary_df.sort_values("Yearly_Return", ascending=False).head(10)
top_losers = summary_df.sort_values("Yearly_Return").head(10)

print("Top 10 Gainers")
print(top_gainers)

print("\nTop 10 Losers")
print(top_losers)


# ------------------ VISUALIZATION ------------------

# Top 10 Gainers Bar Chart
plt.figure()
plt.bar(top_gainers["Ticker"], top_gainers["Yearly_Return"])
plt.title("Top 10 Gainers (Yearly Return)")
plt.xlabel("Stock")
plt.ylabel("Yearly Return")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Losers Bar Chart
plt.figure()
plt.bar(top_losers["Ticker"], top_losers["Yearly_Return"])
plt.title("Top 10 Losers (Yearly Return)")
plt.xlabel("Stock")
plt.ylabel("Yearly Return")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Most Volatile Stocks
top_volatile = summary_df.sort_values("Volatility", ascending=False).head(10)

plt.figure()
plt.bar(top_volatile["Ticker"], top_volatile["Volatility"])
plt.title("Top 10 Most Volatile Stocks")
plt.xlabel("Stock")
plt.ylabel("Volatility")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------ CUMULATIVE RETURN ------------------

top_5_stocks = top_gainers["Ticker"].head(5)

plt.figure()

for ticker in top_5_stocks:
    file_path = os.path.join(csv_folder, f"{ticker}.csv")
    df = pd.read_csv(file_path)

    df["daily_return"] = df["close"].pct_change()
    df["cumulative_return"] = (1 + df["daily_return"]).cumprod()

    plt.plot(df["date"], df["cumulative_return"], label=ticker)

plt.title("Cumulative Return of Top 5 Stocks")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.tight_layout()
plt.show()


# ------------------ SECTOR WISE PERFORMANCE ------------------

print(pd.read_csv("C:/Stock_Analysis_Project/data_reference/sector_mapping.csv").head())

sector_df = pd.read_csv("C:/Stock_Analysis_Project/data_reference/sector_mapping.csv")

# Merge sector info with summary
sector_df["Ticker"] = sector_df["symbol"].str.split(":").str[-1].str.strip()
sector_summary = summary_df.merge(sector_df, on="Ticker", how="inner")

# Average yearly return by sector
sector_performance = (
    sector_summary.groupby("sector")["Yearly_Return"]
    .mean()
    .sort_values(ascending=False)
)

# Plot sector-wise performance
plt.figure()
sector_performance.plot(kind="bar")
plt.title("Average Yearly Return by Sector")
plt.xlabel("Sector")
plt.ylabel("Average Return")
plt.tight_layout()
plt.show()


# ------------------ STOCK PRICE CORRELATION ------------------

close_prices = pd.DataFrame()

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        ticker = file.replace(".csv", "")
        df = pd.read_csv(os.path.join(csv_folder, file))

        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

        close_prices[ticker] = df["close"].values

# Correlation matrix
correlation_matrix = close_prices.corr()

plt.figure(figsize=(12, 10))
plt.imshow(correlation_matrix)
plt.colorbar()

plt.xticks(range(len(correlation_matrix.columns)),
           correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)),
           correlation_matrix.columns)

plt.title("Stock Price Correlation Heatmap")
plt.tight_layout()
plt.show()





