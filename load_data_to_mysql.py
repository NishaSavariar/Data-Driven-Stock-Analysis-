from sqlalchemy import create_engine
import pandas as pd

# Load CSV
df = pd.read_csv("data_powerbi/all_stocks.csv")

# IMPORTANT: URL-encoded password
engine = create_engine(
    "mysql+pymysql://root:Iniya%4008@localhost:3306/stock_db"
)

# Write to MySQL
df.to_sql(
    name="stocks_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data successfully loaded into MySQL!")
