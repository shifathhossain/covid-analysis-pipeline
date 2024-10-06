import yaml
from src.scraper import scrape_data

def load_config(config_path='config/config.yaml'):
    """
    Loads configuration from a YAML file.
    
    Args:
        config_path (str): Path to the configuration file.
    
    Returns:
        dict: Configuration parameters.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def extract():
    """
    Extracts data by scraping the target website.
    
    Returns:
        list of dict: Extracted COVID-19 statistics.
    """
    config = load_config()
    url = config['scraper']['target_url']
    headers = config['scraper']['headers']
    data = scrape_data(url, headers)
    return data
