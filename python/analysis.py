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
import os
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
# ==========================================================
# KEY PERFORMANCE INDICATORS (KPIs)
# ==========================================================

print("\n" + "=" * 70)
print("KEY PERFORMANCE INDICATORS (KPIs)")
print("=" * 70)

# Total Users
total_users = df["Users"].sum()

# Total Sessions
total_sessions = df["Sessions"].sum()

# Total Page Views
total_pageviews = df["PageViews"].sum()

# Average Bounce Rate
avg_bounce_rate = df["BounceRate"].mean()

# Average Session Duration
avg_session_duration = df["SessionDuration"].mean()

# Total Conversions
total_conversions = df["Conversions"].sum()

# Conversion Rate
conversion_rate = (total_conversions / total_sessions) * 100

# Average Pages per Session
pages_per_session = total_pageviews / total_sessions

# Average Users per Day
avg_users_per_day = df.groupby("Date")["Users"].sum().mean()

print(f"Total Users               : {total_users:,}")
print(f"Total Sessions            : {total_sessions:,}")
print(f"Total Page Views          : {total_pageviews:,}")
print(f"Average Bounce Rate       : {avg_bounce_rate:.2f}%")
print(f"Average Session Duration  : {avg_session_duration:.2f} seconds")
print(f"Total Conversions         : {total_conversions:,}")
print(f"Conversion Rate           : {conversion_rate:.2f}%")
print(f"Pages Per Session         : {pages_per_session:.2f}")
print(f"Average Users Per Day     : {avg_users_per_day:.2f}")

print("\n")

# ==========================================================
# HIGHEST AND LOWEST VALUES
# ==========================================================

print("=" * 70)
print("PERFORMANCE HIGHLIGHTS")
print("=" * 70)

highest_users = df.loc[df["Users"].idxmax()]
lowest_users = df.loc[df["Users"].idxmin()]

print("Highest Traffic Day")
print("-------------------")
print(f"Date      : {highest_users['Date'].date()}")
print(f"Users     : {highest_users['Users']}")
print(f"Sessions  : {highest_users['Sessions']}")
print()

print("Lowest Traffic Day")
print("------------------")
print(f"Date      : {lowest_users['Date'].date()}")
print(f"Users     : {lowest_users['Users']}")
print(f"Sessions  : {lowest_users['Sessions']}")

print("\n")

# ==========================================================
# MONTHLY KPI SUMMARY
# ==========================================================

print("=" * 70)
print("MONTHLY PERFORMANCE SUMMARY")
print("=" * 70)

monthly_summary = (
    df.groupby("Month")
    .agg({
        "Users": "sum",
        "Sessions": "sum",
        "PageViews": "sum",
        "Conversions": "sum"
    })
)

print(monthly_summary)

print("\n")

# ==========================================================
# DEVICE-WISE USERS
# ==========================================================

print("=" * 70)
print("DEVICE PERFORMANCE")
print("=" * 70)

device_summary = (
    df.groupby("Device")["Users"]
    .sum()
    .sort_values(ascending=False)
)

print(device_summary)

print("\n")

# ==========================================================
# TRAFFIC SOURCE PERFORMANCE
# ==========================================================

print("=" * 70)
print("TRAFFIC SOURCE PERFORMANCE")
print("=" * 70)

traffic_summary = (
    df.groupby("TrafficSource")
    .agg({
        "Users": "sum",
        "Sessions": "sum",
        "Conversions": "sum"
    })
    .sort_values(by="Users", ascending=False)
)

print(traffic_summary)

print("\n")

# ==========================================================
# COUNTRY PERFORMANCE
# ==========================================================

print("=" * 70)
print("TOP COUNTRIES")
print("=" * 70)

country_summary = (
    df.groupby("Country")["Users"]
    .sum()
    .sort_values(ascending=False)
)

print(country_summary)

print("\n")

print("=" * 70)
print("KPI ANALYSIS COMPLETED")
print("=" * 70)
