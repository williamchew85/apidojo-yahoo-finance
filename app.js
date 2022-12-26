const express = require("express");
const app = express();
const port = 3000;

const PythonShell = require("python-shell");

app.get("/api/stock-data", (req, res) => {
  // Run the Python script using PythonShell
  PythonShell.run("stock_data.py", (err, data) => {
    if (err) throw err;
    res.send(data);
  });
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
