import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [stockData, setStockData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      // Make a GET request to the Node.js backend to retrieve stock data
      const response = await axios.get("http://localhost:3000/api/stock-data");
      setStockData(response.data);
    }
    fetchData();
  }, []);

  if (stockData) {
    // Extract the date and close price data from the response
    const dates = stockData.dates;
    const prices = stockData.prices;

    // Render the chart using the data
    return (
      <div>
        <h1>AAPL Stock Prices</h1>
        <p>Dates: {dates.join(", ")}</p>
        <p>Prices: {prices.join(", ")}</p>
      </div>
    );
  } else {
    // Render a loading message while the data is being retrieved
    return <p>Loading...</p>;
  }
}

export default App;
