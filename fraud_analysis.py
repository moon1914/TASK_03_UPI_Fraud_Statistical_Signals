import pandas as pd

# Load dataset
df = pd.read_csv("../data/fraud_dataset.csv")

# Basic information
print("Dataset Shape:", df.shape)

# Fraud distribution
print("\nFraud Distribution:")
print(df["is_fraud"].value_counts())

# Average transaction amount
print("\nAverage Transaction Amount:")
print(df.groupby("is_fraud")["amount"].mean())

# High-value transaction threshold
Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR

print("\nHigh-Value Transaction Threshold:", upper_limit)

# Count high-value transactions
high_value = df[df["amount"] > upper_limit]
print("High-Value Transactions:", len(high_value))