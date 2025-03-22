# Objective: This project scrapes real-time stock data (company name, price, change, and volume) from the Groww website 
# for selected US and Indian stocks, and exports the collected data to an Excel file.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

urls = [
    'https://groww.in/us-stocks/nke',
    'https://groww.in/us-stocks/ko',
    'https://groww.in/us-stocks/msft',
    'https://groww.in/stocks/m-india-ltd',
    'https://groww.in/us-stocks/axp',
    'https://groww.in/us-stocks/aapl',
    'https://groww.in/us-stocks/intc'
]

all_data = []

for url in urls:
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        company = soup.find('h1').text
        price = soup.find('span', {'class': 'uht141Pri'}).text
        change = soup.find('div', {'class': 'uht141Day'}).text
        volume = soup.find('table').find_all('td')[1].text

        all_data.append([company, price, change, volume])
        print(f"Scraped: {company}")

    except AttributeError as e:
        print(f"Error scraping {url}: {e}")
    except Exception as e:
        print(f"Unexpected error on {url}: {e}")

    time.sleep(5)

df = pd.DataFrame(all_data, columns=["Company", "Price", "Change", "Volume"])
df.to_excel('stocks.xlsx', index=False)

print("Data saved to 'stocks.xlsx'.")
