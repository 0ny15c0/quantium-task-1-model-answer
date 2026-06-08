import pandas as pd

# Read the three CSV files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all data into one DataFrame
df = pd.concat([df0, df1, df2], ignore_index=True)

# Keep only pink morsel sales
df = df[df["product"] == "pink morsel"]

# Remove the '$' sign from price and convert to float
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create the Sales column
df["Sales"] = df["quantity"] * df["price"]

# Keep only the required columns
output = df[["Sales", "date", "region"]]

# Rename columns to match requirements
output.columns = ["Sales", "Date", "Region"]

# Save the output to a CSV file
output.to_csv("formatted_output.csv", index=False)

print("formatted_output.csv created successfully")
