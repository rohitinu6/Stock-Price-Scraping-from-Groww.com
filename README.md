# 📈 Stock Price Scraping from Groww.com

This project scrapes real-time stock data (company name, price, change, and volume) from the Groww website for selected US and Indian stocks. The collected data is then exported to an Excel file.

## 🛠️ Features

- Scrapes real-time stock information (Company Name, Price, Change, Volume)
- Supports multiple US and Indian stocks
- Exports the collected data to an Excel file (`stocks.xlsx`)
- Error handling for failed requests

## 📊 Technologies Used

- Python
- Requests (for HTTP requests)
- BeautifulSoup (for web scraping)
- Pandas (for data manipulation and Excel export)

## 📥 Installation

1. Clone the repository:

```bash
   git clone https://github.com/rohitinu6/rohitinu6-Stock-Price-Scraping-from-Groww.com.git
   cd rohitinu6-Stock-Price-Scraping-from-Groww.com
```

2. Set up a virtual environment (optional but recommended):

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
   pip install -r requirements.txt
```

## 🚀 Usage

1. Run the scraper:

```bash
   python scraper.py
```

2. After execution, the scraped data will be saved to `stocks.xlsx` in the project directory.

## 📄 Code Explanation

1. **Headers Setup**: Simulates a browser request using a user-agent.
2. **URLs List**: Contains Groww stock URLs to scrape.
3. **Web Scraping**: Requests each URL, parses the HTML, and extracts the company name, price, change, and volume.
4. **Data Export**: Saves the collected data into an Excel file using Pandas.

## 🐛 Error Handling

- Handles missing data with `AttributeError`.
- Prints meaningful error messages for better debugging.

## 📌 Dependencies

Ensure the following Python packages are installed:

- requests
- beautifulsoup4
- pandas

You can install them using:

```bash
pip install requests beautifulsoup4 pandas
```

## 📧 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

⭐️ Don't forget to give a star if you find this project useful!

