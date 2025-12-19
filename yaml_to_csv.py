import yaml
import pandas as pd
import os

# Base folders
yaml_base_folder = "C:/Stock_Analysis_Project/data_yaml"
csv_output_folder = "C:/Stock_Analysis_Project/data_csv"

# Create CSV output folder if not exists
os.makedirs(csv_output_folder, exist_ok=True)

# Loop through each month folder
for month_folder in os.listdir(yaml_base_folder):
    month_path = os.path.join(yaml_base_folder, month_folder)

    # Check if it is a folder
    if os.path.isdir(month_path):

        # Loop through each YAML file in month folder
        for yaml_file in os.listdir(month_path):
            if yaml_file.endswith(".yaml") or yaml_file.endswith(".yml"):

                yaml_path = os.path.join(month_path, yaml_file)

                # Read YAML file
                with open(yaml_path, "r") as file:
                    stock_data = yaml.safe_load(file)

                # Convert to DataFrame
                df = pd.DataFrame(stock_data)

                # Group by Ticker and save CSV
                for ticker, group in df.groupby("Ticker"):
                    csv_file_path = os.path.join(csv_output_folder, f"{ticker}.csv")

                    # Append if file exists
                    if os.path.exists(csv_file_path):
                        group.to_csv(csv_file_path, mode="a", header=False, index=False)
                    else:
                        group.to_csv(csv_file_path, index=False)

                print(f"Processed {yaml_file} from {month_folder}")
