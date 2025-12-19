import pandas as pd
import os

csv_folder = "C:/Stock_Analysis_Project/data_csv"

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(csv_folder, file)

        df = pd.read_csv(file_path)

        # Convert date column
        df["date"] = pd.to_datetime(df["date"])

        # Sort by date
        df = df.sort_values("date")

        # Remove duplicates
        df = df.drop_duplicates()

        # Reorder columns
        df = df[["Ticker", "date", "open", "high", "low", "close", "volume", "month"]]

        # Save cleaned file
        df.to_csv(file_path, index=False)

        print(f"Cleaned {file}")
