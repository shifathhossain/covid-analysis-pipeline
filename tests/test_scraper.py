import pytest
from src.scraper import scrape_data

def test_scrape_data_success(monkeypatch):
    """
    Tests that scrape_data successfully returns a list of dictionaries.
    """
    sample_html = """
    <html>
        <body>
            <table id="main_table_countries_today">
                <tbody>
                    <tr>
                        <td></td>
                        <td>CountryA</td>
                        <td>1000</td>
                        <td>50</td>
                        <td>25</td>
                        <td>5</td>
                        <td>900</td>
                        <td></td>
                        <td>75</td>
                        <td>10</td>
                        <td>5000</td>
                        <td>250</td>
                        <td>15000</td>
                        <td>750</td>
                        <td>2000000</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>
    """
    class MockResponse:
        def __init__(self, text, status_code=200):
            self.text = text
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.HTTPError(f"{self.status_code} Error")

    def mock_get(*args, **kwargs):
        return MockResponse(sample_html)

    monkeypatch.setattr('requests.get', mock_get)

    url = "https://www.worldometers.info/coronavirus/"
    headers = {"User-Agent": "TestAgent"}
    data = scrape_data(url, headers)
    
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['country'] == 'CountryA'
    assert data[0]['total_cases'] == 1000
    assert data[0]['new_cases'] == 50
    assert data[0]['total_deaths'] == 25
    assert data[0]['new_deaths'] == 5
    assert data[0]['total_recovered'] == 900
    assert data[0]['active_cases'] == 75
    assert data[0]['serious_critical'] == 10
    assert data[0]['total_cases_per_million'] == 5000.0
    assert data[0]['total_deaths_per_million'] == 250.0
    assert data[0]['total_tests'] == 15000
    assert data[0]['tests_per_million'] == 750.0
    assert data[0]['population'] == 2000000
