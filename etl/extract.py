import yaml
import logging
from src.scraper import scrape_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path='config/configure.yml'):
    """
    Loads configuration from a YAML file.
    
    Args:
        config_path (str): Path to the configuration file.
    
    Returns:
        dict: Configuration parameters.
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found at {config_path}")
        raise
    except yaml.YAMLError as exc:
        logging.error(f"Error parsing YAML file: {exc}")
        raise

def extract():
    """
    Extracts data by scraping the target website.
    
    Returns:
        list of dict: Extracted COVID-19 statistics.
    """
    config = load_config()
    url = config['scraper']['target_url']
    headers = config['scraper']['headers']
    logging.info(f"Starting data extraction from {url}")
    data = scrape_data(url, headers)
    return data
