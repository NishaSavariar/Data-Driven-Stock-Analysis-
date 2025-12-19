import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")

st.title("📊 Data-Driven Stock Analysis")

# ---------------- LOAD DATA ----------------
DATA_FOLDER = "data_csv"

all_data = []

for file in os.listdir(DATA_FOLDER):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(DATA_FOLDER, file))
        df["Ticker"] = file.replace(".csv", "")
        all_data.append(df)

# Combine all CSVs
data = pd.concat(all_data, ignore_index=True)

# Date conversion
data["date"] = pd.to_datetime(data["date"])

# ---------------- CALCULATIONS ----------------
data = data.sort_values(["Ticker", "date"])
data["Daily_Return"] = data.groupby("Ticker")["close"].pct_change()

summary = data.groupby("Ticker").agg(
    Yearly_Return=("close", lambda x: x.iloc[-1] / x.iloc[0] - 1),
    Volatility=("Daily_Return", "std")
).reset_index()

# Normalize ticker format (VERY IMPORTANT)
summary["Ticker"] = summary["Ticker"].str.strip().str.upper()
data["Ticker"] = data["Ticker"].str.strip().str.upper()

# ---------------- SIDEBAR ----------------
st.sidebar.header("Stock Selection")

selected_stock = st.sidebar.selectbox(
    "Select a Stock",
    sorted(data["Ticker"].unique())
)

stock_data = data[data["Ticker"] == selected_stock].sort_values("date")

# ---------------- PRICE TREND ----------------
st.subheader(f"📈 Closing Price Trend – {selected_stock}")

fig, ax = plt.subplots()
ax.plot(stock_data["date"], stock_data["close"])
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

st.pyplot(fig)

# ---------------- STOCK SUMMARY ----------------
st.subheader("📌 Stock Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Start Price", round(stock_data["close"].iloc[0], 2))
col2.metric("End Price", round(stock_data["close"].iloc[-1], 2))

yearly_return = stock_data["close"].iloc[-1] / stock_data["close"].iloc[0] - 1
col3.metric("Yearly Return", f"{yearly_return:.2%}")

# ---------------- TOP GAINERS / LOSERS ----------------
st.subheader("🏆 Top 10 Gainers & Losers")

col1, col2 = st.columns(2)

top_gainers = summary.sort_values("Yearly_Return", ascending=False).head(10)
top_losers = summary.sort_values("Yearly_Return").head(10)

col1.write("### 🟢 Top 10 Gainers")
col1.dataframe(top_gainers.style.format({"Yearly_Return": "{:.2%}"}))

col2.write("### 🔴 Top 10 Losers")
col2.dataframe(top_losers.style.format({"Yearly_Return": "{:.2%}"}))

# ---------------- VOLATILITY ----------------
st.subheader("⚠️ Top 10 Most Volatile Stocks")

volatile_stocks = summary.sort_values("Volatility", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(volatile_stocks["Ticker"], volatile_stocks["Volatility"])

ax.set_xlabel("Stock")
ax.set_ylabel("Volatility")
ax.set_title("Top 10 Most Volatile Stocks")

# FIX X-axis readability
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
st.pyplot(fig)


# ---------------- SECTOR ANALYSIS (SAFE & FIXED) ----------------
st.subheader("🏭 Sector-wise Average Performance")

sector_df = pd.read_csv("data_reference/sector_clean.csv")

# Normalize sector tickers
sector_df["Ticker"] = sector_df["Ticker"].str.strip().str.upper()

# Debug display (can be removed later)
#st.write("Sample Stock Tickers:", summary["Ticker"].unique()[:10])
#st.write("Sample Sector Tickers:", sector_df["Ticker"].unique()[:10])

sector_summary = summary.merge(sector_df, on="Ticker", how="inner")

if sector_summary.empty:
    st.warning("Sector data not matching with stock tickers.")
else:
    sector_perf = sector_summary.groupby("sector")["Yearly_Return"].mean().sort_values(ascending=False)

    fig, ax = plt.subplots()
    sector_perf.plot(kind="bar", ax=ax)
    ax.set_ylabel("Average Yearly Return")
    ax.set_title("Sector-wise Average Performance")

    st.pyplot(fig)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("📌 **Project:** Data-Driven Stock Analysis")
st.markdown("📌 **Tools:** Python, Pandas, Streamlit, Power BI, MySQL")
st.markdown("📌 **Author:** Nisha")
