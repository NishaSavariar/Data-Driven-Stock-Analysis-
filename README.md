📊 Data-Driven Stock Analysis 

Project Overview
This project focuses on analyzing and visualizing the performance of Nifty 50 stocks over a one-year period using a data-driven approach. The solution processes raw stock market data, calculates key financial metrics, stores data in a relational database, and presents insights through Python analysis, an interactive Streamlit dashboard, MySQL SQL queries, and Power BI dashboards.
The project is designed for beginners and follows industry-standard workflows used in real-world data analytics projects.
________________________________________
Business Objectives
•	Identify Top 10 Gainers and Top 10 Losers based on yearly returns
•	Provide a market overview using KPIs
•	Analyze sector-wise performance
•	Understand stock price correlation
•	Track monthly gainers and losers
•	Support investment decision-making using data insights
•	Validate analytical results using SQL queries
________________________________________
Tools & Technologies
1) Languages & Libraries
•	Python 3.11
•	Pandas
•	NumPy
•	Matplotlib
•	PyYAML
•	SQLAlchemy
2) Visualization Tools
•	Streamlit (Interactive Dashboard)
•	Power BI Desktop

3) Databases
•	MySQL (Database)
________________________________________
Project Architecture
Stock_Analysis_Project/
│
├── data_yaml/                 
├── data_csv/                  
├── data_reference/          
├── data_powerbi/
├──          
├── scripts/
│   ├── yaml_to_csv.py        
│   ├── analysis.py            
│   ├── create_powerbi_csv.py  
│
├── load_data_to_mysql.py      
├── dashboard.py               
├── README.md                  
└── requirements.txt           
________________________________________
Project Workflow (End-to-End)
Step 1: Data Collection
•	Input data provided in YAML format
•	Organized into month-wise folders
•	Each YAML file contains daily stock data
________________________________________
Step 2: Data Extraction & Cleaning
•	YAML files are parsed using Python
•	Data is cleaned and standardized
•	Output: 50 CSV files, one per stock
Script used:
python scripts/yaml_to_csv.py
________________________________________
Step 3: Data Analysis (Python)
Using Pandas, the following metrics are calculated:
•	Daily Returns
•	Yearly Returns
•	Volatility (Standard Deviation of daily returns)
•	Cumulative Returns
•	Monthly Returns
Script used:
python scripts/analysis.py
________________________________________
Step 4: Database Storage (MySQL)
•	Cleaned stock data is loaded into MySQL using Pandas and SQLAlchemy
•	Enables SQL-based validation for top 10 gainers & losers of analytical results
•	Ensures consistency across Python, Streamlit, and Power BI
Script used:
python load_data_to_mysql.py
________________________________________
Step 5: Streamlit Dashboard
An interactive dashboard built using Streamlit to visualize:
•	Stock price trends
•	Top gainers & losers
•	Sector-wise performance
•	Monthly analysis
Run the dashboard:
streamlit run dashboard.py
________________________________________

Step 6: Power BI Data Preparation
•	All stock CSVs are combined into a single dataset
•	Sector mapping is merged
•	Output: Power BI–ready CSV file
Script used:
python scripts/create_powerbi_csv.py
________________________________________
Step 7: Power BI Dashboard
Power BI is used to build:
•	KPI cards (Market overview)
•	Top gainers & losers
•	Sector-wise performance
•	Correlation heatmap
•	Monthly gainers & losers
________________________________________
Key Visualizations
•	Stock Price Trend (Month-wise)
•	Top 10 Gainers (Yearly)
•	Top 10 Losers (Yearly)
•	Sector-wise Average Return
•	Correlation Heatmap
•	Top 5 Gainers & Losers (Monthly)
________________________________________
Project Deliverables
•	Cleaned CSV datasets
•	Python scripts for ETL & analysis
•	Streamlit interactive dashboard
•	Power BI dashboard
•	Well-documented GitHub repository
________________________________________

How to Run This Project
1.Install dependencies
pip install -r requirements.txt
2.Convert YAML to CSV
python scripts/yaml_to_csv.py
3.Run analysis
python scripts/analysis.py
4. Load data into MySQL
python load_data_to_mysql.py
5.Launch Streamlit app
streamlit run dashboard.py
6.Open Power BI
•	Load data_powerbi/all_stocks.csv
•	Build visuals using Power BI Desktop
________________________________________
Coding Standards Followed
•	Modular scripts
•	Meaningful variable names
•	Beginner-friendly logic
•	Inline comments for clarity
________________________________________
Future Enhancements
•	Live stock data integration (API)
•	Automated database refresh
•	Deployment on Streamlit Cloud
•	Advanced risk metrics (Sharpe Ratio, Beta)
________________________________________




Demo Video Link
https://www.linkedin.com/posts/nisha-savariar_datascience-dataanalytics-python-activity-7407864354995576833-snPD?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFmmQMIB0iVcomJx8dDIIc6t9Wu0MBIP9wE
________________________________________
👩‍💻 Author
Nisha
Data Science Project – Stock Market Analysis
⭐ If you find this project useful, feel free to star the repository!



