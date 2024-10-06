#### **a. Web Scraper**

import requests
from bs4 import BeautifulSoup

def fetch_page(url, headers):
    """
    Fetches the HTML content of the target URL.
    
    Args:
        url (str): The URL to scrape.
        headers (dict): HTTP headers to include in the request.
    
    Returns:
        str: HTML content of the page.
    
    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html):
    """
    Parses the HTML content and extracts COVID-19 statistics.
    
    Args:
        html (str): HTML content of the page.
    
    Returns:
        list of dict: List containing COVID-19 statistics per country.
    """
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', id='main_table_countries_today')
    if not table:
        raise ValueError("No table found with id 'main_table_countries_today'")

    data = []
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 15:
            continue  # Skip incomplete rows

        country_data = {
            'country': cols[1].text.strip(),
            'total_cases': parse_int(cols[2].text),
            'new_cases': parse_int(cols[3].text),
            'total_deaths': parse_int(cols[4].text),
            'new_deaths': parse_int(cols[5].text),
            'total_recovered': parse_int(cols[6].text),
            'active_cases': parse_int(cols[8].text),
            'serious_critical': parse_int(cols[9].text),
            'total_cases_per_million': parse_float(cols[10].text),
            'total_deaths_per_million': parse_float(cols[11].text),
            'total_tests': parse_int(cols[12].text),
            'tests_per_million': parse_float(cols[13].text),
            'population': parse_int(cols[14].text),
        }
        data.append(country_data)
    return data

def parse_int(value):
    """
    Parses a string to an integer, handling special cases.
    
    Args:
        value (str): The string to parse.
    
    Returns:
        int or None: Parsed integer or None if not available.
    """
    value = value.replace(',', '').replace('+', '').strip()
    return int(value) if value.isdigit() else None

def parse_float(value):
    """
    Parses a string to a float, handling special cases.
    
    Args:
        value (str): The string to parse.
    
    Returns:
        float or None: Parsed float or None if not available.
    """
    value = value.replace(',', '').replace('+', '').strip()
    try:
        return float(value)
    except ValueError:
        return None

def scrape_data(url, headers):
    """
    Scrapes COVID-19 data from the specified URL.
    
    Args:
        url (str): The URL to scrape.
        headers (dict): HTTP headers to include in the request.
    
    Returns:
        list of dict: List containing COVID-19 statistics per country.
    """
    html = fetch_page(url, headers)
    data = parse_html(html)
    return data
