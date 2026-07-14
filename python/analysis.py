"""
Project: Website Traffic Analytics Dashboard
Author: Kinjal Dalwadi

Description:
This project analyzes website traffic data to understand user behavior,
traffic sources, website engagement, and conversion performance.

Tools:
- Python
- Pandas
- NumPy
- Matplotlib

"""

# ===============================
# Import Required Libraries
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display all columns
pd.set_option('display.max_columns', None)

print("=" * 70)
print("WEBSITE TRAFFIC ANALYTICS DASHBOARD")
print("=" * 70)

# ===============================
# Load Dataset
# ===============================

try:
    df = pd.read_csv("data/website_traffic.csv")
    print("\nDataset loaded successfully.\n")
except FileNotFoundError:
    print("Dataset not found.")
    exit()

# ===============================
# Basic Information
# ===============================

print("=" * 70)
print("FIRST FIVE RECORDS")
print("=" * 70)

print(df.head())

print("\n")

print("=" * 70)
print("LAST FIVE RECORDS")
print("=" * 70)

print(df.tail())

print("\n")

print("=" * 70)
print("DATASET SHAPE")
print("=" * 70)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\n")

print("=" * 70)
print("COLUMN NAMES")
print("=" * 70)

print(df.columns.tolist())

print("\n")

print("=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)

print("\n")

print("=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

df.info()

print("\n")

# ===============================
# Summary Statistics
# ===============================

print("=" * 70)
print("SUMMARY STATISTICS")
print("=" * 70)

print(df.describe())

print("\n")

# ===============================
# Missing Values
# ===============================

print("=" * 70)
print("MISSING VALUES")
print("=" * 70)

missing = df.isnull().sum()

print(missing)

print("\n")

# ===============================
# Duplicate Records
# ===============================

print("=" * 70)
print("DUPLICATE RECORDS")
print("=" * 70)

duplicates = df.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")

print("\n")

# ===============================
# Convert Date
# ===============================

print("=" * 70)
print("DATE CONVERSION")
print("=" * 70)

df["Date"] = pd.to_datetime(df["Date"])

print(df["Date"].head())

print("\n")

# ===============================
# Create Additional Columns
# ===============================

print("=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)

df["Year"] = df["Date"].dt.year

df["Month"] = df["Date"].dt.month_name()

df["Day"] = df["Date"].dt.day_name()

print(df.head())

print("\n")

# ===============================
# Check Unique Values
# ===============================

print("=" * 70)
print("UNIQUE VALUES")
print("=" * 70)

print("Traffic Sources")

print(df["TrafficSource"].unique())

print("\n")

print("Devices")

print(df["Device"].unique())

print("\n")

print("Countries")

print(df["Country"].unique())

print("\n")

# ===============================
# Dataset Ready
# ===============================

print("=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)

print("Dataset is ready for Exploratory Data Analysis (EDA).")
