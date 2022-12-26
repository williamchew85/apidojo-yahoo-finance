# python-apidojo-yahoo-finance
Example of a Python script that demonstrates how to use the Yahoo Finance API from RapidAPI to retrieve data for a specific stock

# index.js
Landing page for React.js

# app.js
This backend script uses the python-shell module to run the Python script that retrieves stock data from the Yahoo Finance API. The script then sends the data back to the frontend as a response to the GET request.

On the frontend, the React.js component makes a GET request to the backend to retrieve the stock data and displays it on the page.

# stock_data.py
This script defines a YahooFinanceAPI class that encapsulates the logic for making requests to the Yahoo Finance API. The class has a single method, get_stock_data, which takes a stock symbol, interval, and range as input and returns data for the specified stock.

To use this script, you will need to sign up for an API key and replace "YOUR_API_KEY" in the script with your actual API key.
