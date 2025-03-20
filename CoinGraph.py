import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

def getBinanceData(interval, limit, coin):
    url = f"https://api.binance.com/api/v3/klines?symbol={coin}USDT&interval={interval}h&limit={limit}"  
    response = requests.get(url)
    data = response.json()
    
    # Defining the columns
    columns = [
        "Open Time", "Open Price", "High Price", "Low Price", "Close Price", 
        "Volume", "Close Time", "Quote Asset Volume", "Number of Trades", 
        "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Unused"
    ]
    df = pd.DataFrame(data, columns=columns)
    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
    df['Close Price'] = pd.to_numeric(df['Close Price'])
    
    return df

coin = input("Enter the coin name: ")
df = getBinanceData(1, 100, coin.upper())

# Plot the data
plt.plot(df['Open Time'], df['Close Price'], marker='', color='blue')

plt.ylabel("Close Price")
plt.xlabel("Time")
plt.grid()
plt.xticks(rotation=45)  # Rotate x-axis labels to avoid overlap
plt.show()
