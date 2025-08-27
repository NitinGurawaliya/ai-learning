# 📊 DAY 2: Python for Data & APIs - Your Data Science Foundation
# ================================================================

print("🚀 Welcome to Day 2 of your AI Learning Journey!")
print("Today we'll master data manipulation, visualization, and API integration.\n")

# ============================================================================
# 1. PANDAS BASICS - Data Manipulation Powerhouse
# ============================================================================

print("🐼 SECTION 1: Pandas Basics")
print("-" * 50)

import pandas as pd
import numpy as np

print("✅ Pandas imported successfully!")

# Creating DataFrames (2D data structure like Excel)
print("\n--- Creating DataFrames ---")

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Miami'],
    'Salary': [75000, 85000, 90000, 80000]
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)
print(f"\nDataFrame shape: {df.shape}")
print(f"DataFrame columns: {list(df.columns)}")

print("\n" + "="*60 + "\n")

# ============================================================================
# 2. PANDAS DATA MANIPULATION
# ============================================================================

print("🔧 SECTION 2: Pandas Data Manipulation")
print("-" * 50)

# Indexing and selection
print("--- Indexing and Selection ---")
print("First 2 rows:")
print(df.head(2))

print("\nSelect specific columns:")
print(df[['Name', 'Salary']])

print("\nSelect rows by condition:")
high_salary = df[df['Salary'] > 80000]
print("People with salary > $80,000:")
print(high_salary)

# Grouping and aggregation
print("\n--- Grouping and Aggregation ---")
print("Average salary by city:")
city_salary = df.groupby('City')['Salary'].mean()
print(city_salary)

# Adding new columns
print("\n--- Adding New Columns ---")
df['Salary_K'] = df['Salary'] / 1000  # Convert to thousands
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
print("DataFrame with new columns:")
print(df)

print("\n" + "="*60 + "\n")

# ============================================================================
# 3. MATPLOTLIB - Basic Data Visualization
# ============================================================================

print("📈 SECTION 3: Matplotlib - Data Visualization")
print("-" * 50)

import matplotlib.pyplot as plt

# Set style for better-looking plots
plt.style.use('default')

# Line plot
print("--- Creating Line Plot ---")
plt.figure(figsize=(10, 6))

# Sample time series data
dates = pd.date_range('2024-01-01', periods=30, freq='D')
values = np.random.randn(30).cumsum()  # Random walk

plt.plot(dates, values, linewidth=2, color='blue', marker='o', markersize=4)
plt.title('Sample Time Series Data', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('week1/line_plot.png', dpi=300, bbox_inches='tight')
print("✅ Line plot saved as 'line_plot.png'")

print("\n" + "="*60 + "\n")

# ============================================================================
# 4. SEABORN - Statistical Data Visualization
# ============================================================================

print("🎨 SECTION 4: Seaborn - Statistical Visualization")
print("-" * 50)

import seaborn as sns

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Distribution plot
print("--- Creating Distribution Plot ---")
plt.figure(figsize=(10, 6))

sns.histplot(data=df, x='Salary', bins=10, kde=True, color='skyblue')
plt.title('Salary Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Salary ($)', fontsize=12)
plt.ylabel('Count', fontsize=12)

plt.tight_layout()
plt.savefig('week1/distribution_plot.png', dpi=300, bbox_inches='tight')
print("✅ Distribution plot saved as 'distribution_plot.png'")

print("\n" + "="*60 + "\n")

# ============================================================================
# 5. REQUESTS LIBRARY - Working with APIs
# ============================================================================

print("🌐 SECTION 5: Requests Library - API Integration")
print("-" * 50)

import requests
import json
from datetime import datetime, timedelta

print("✅ Requests library imported successfully!")

# Basic GET request
print("\n--- Basic GET Request ---")
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    post_data = response.json()
    print("Sample API response:")
    print(f"Title: {post_data['title']}")
    print(f"Body: {post_data['body'][:100]}...")
else:
    print(f"Error: {response.status_code}")

print("\n" + "="*60 + "\n")

# ============================================================================
# 🎯 PRACTICE PROJECT: Bitcoin Price Analysis
# ============================================================================

print("🎯 PRACTICE PROJECT: Bitcoin Price Analysis")
print("-" * 50)

# Working with CoinGecko API (free, no API key required)
print("--- CoinGecko API - Bitcoin Data ---")

try:
    # Get Bitcoin price data
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': '30',
        'interval': 'daily'
    }
    
    print("Fetching Bitcoin price data...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        bitcoin_data = response.json()
        
        # Extract price data
        prices = bitcoin_data['prices']
        dates = [datetime.fromtimestamp(price[0]/1000) for price in prices]
        prices_usd = [price[1] for price in prices]
        
        print(f"✅ Successfully fetched {len(prices)} data points")
        print(f"Latest Bitcoin price: ${prices_usd[-1]:,.2f}")
        print(f"Price 30 days ago: ${prices_usd[0]:,.2f}")
        
        # Calculate price change
        price_change = ((prices_usd[-1] - prices_usd[0]) / prices_usd[0]) * 100
        print(f"30-day price change: {price_change:+.2f}%")
        
        # Create DataFrame for analysis
        btc_df = pd.DataFrame({
            'Date': dates,
            'Price_USD': prices_usd
        })
        
        print(f"\nBitcoin DataFrame shape: {btc_df.shape}")
        print("\nFirst few rows:")
        print(btc_df.head())
        
        # Create Bitcoin price chart
        plt.figure(figsize=(12, 6))
        plt.plot(btc_df['Date'], btc_df['Price_USD'], linewidth=2, color='orange', marker='o', markersize=3)
        plt.title('Bitcoin Price Trend (30 Days)', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Price (USD)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig('week1/bitcoin_price.png', dpi=300, bbox_inches='tight')
        print("✅ Bitcoin price chart saved as 'bitcoin_price.png'")
        
    else:
        print(f"Error fetching Bitcoin data: {response.status_code}")
        
except Exception as e:
    print(f"Error: {e}")
    print("Creating sample Bitcoin data for demonstration...")
    
    # Create sample data if API fails
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    np.random.seed(42)
    base_price = 45000
    prices_usd = [base_price + np.random.normal(0, 1000) for _ in range(30)]
    
    btc_df = pd.DataFrame({
        'Date': dates,
        'Price_USD': prices_usd
    })

print("\n" + "="*60 + "\n")

# ============================================================================
# 📝 SUMMARY & NEXT STEPS
# ============================================================================

print("📝 DAY 2 SUMMARY")
print("-" * 50)

print("✅ What you learned today:")
print("  • Pandas: Data manipulation, filtering, grouping, aggregation")
print("  • Matplotlib: Line plots, bar charts, scatter plots")
print("  • Seaborn: Statistical visualizations, heatmaps, distributions")
print("  • Requests: API integration and data fetching")
print("  • Real-world project: Bitcoin price analysis")

print("\n🎯 Key concepts for AI/ML:")
print("  • Data preprocessing and cleaning with Pandas")
print("  • Exploratory data analysis (EDA)")
print("  • Data visualization for insights")
print("  • API integration for real-time data")

print("\n🚀 Tomorrow: Math for AI (Linear Algebra, Probability, Gradient Descent)")
print("Get ready to understand the mathematical foundations of AI!")

print("\n" + "="*60)
print("🎉 Congratulations on completing Day 2! 🎉")
print("You can now work with real data and create professional visualizations!")

# Close all plots to free memory
plt.close('all')
