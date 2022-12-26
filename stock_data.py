import requests
import matplotlib.pyplot as plt

class YahooFinanceAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com"

    def get_stock_data(self, symbol, interval, range):
        """Retrieve data for a specific stock from the Yahoo Finance API."""
        endpoint = "/stock/v2/get-chart"
        url = self.base_url + endpoint
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        params = {
            "symbol": symbol,
            "interval": interval,
            "range": range
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code}

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Create an instance of the YahooFinanceAPI class
api = YahooFinanceAPI(api_key)

# Retrieve data for the stock symbol "AAPL"
data = api.get_stock_data("AAPL", "1d", "1d")

# Extract the date and close price data from the response
dates = [item["date"] for item in data["chart"]["result"][0]["timestamp"]]
prices = [item["close"] for item in data["chart"]["result"][0]["indicators"]["quote"][0]["close"]]

# Plot the data using Matplotlib
plt.plot(dates, prices)
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("AAPL Stock Prices")
plt.show()
