import requests
from bs4 import BeautifulSoup
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_data(url, headers):
    try:
        logging.info(f"Fetching data from {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id='main_table_countries_today')

        if not table:
            logging.error("COVID-19 data table not found on the page")
            raise ValueError("Data table not found")

        data = []
        rows = table.find_all('tr')[1:]  # Skip header row

        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 7:  # Ensure that each row has enough columns
                continue
            country_data = {
                'country': cols[1].text.strip(),
                'total_cases': cols[2].text.strip().replace(',', ''),
                'new_cases': cols[3].text.strip().replace(',', ''),
                'total_deaths': cols[4].text.strip().replace(',', ''),
                'total_recovered': cols[5].text.strip().replace(',', ''),
                'active_cases': cols[6].text.strip().replace(',', ''),
            }
            data.append(country_data)

        logging.info(f"Successfully scraped {len(data)} records.")
        return data

    except requests.RequestException as e:
        logging.error(f"Failed to retrieve data: {e}")
        raise
