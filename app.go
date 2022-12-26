package main

import (
	"fmt"
	"net/http"
	"os/exec"
	"io/ioutil"
)

func main() {
	http.HandleFunc("/api/stock-data", func(w http.ResponseWriter, r *http.Request) {
		// Run the Python script using exec.Command
		out, err := exec.Command("python", "stock_data.py").Output()
		if err != nil {
			fmt.Fprintf(w, "Error: %s", err)
		} else {
			// Send the data returned by the Python script as the response
			w.Write(out)
		}
	})

	http.ListenAndServe(":3000", nil)
}
