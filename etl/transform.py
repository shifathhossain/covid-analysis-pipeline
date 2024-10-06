import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform(data):
    """
    Transforms raw data into a structured DataFrame.

    Args:
        data (list of dict): Raw COVID-19 statistics.

    Returns:
        pd.DataFrame: Transformed and cleaned data.
    """
    try:
        logging.info("Starting data transformation...")
        df = pd.DataFrame(data)

        df['total_cases'] = pd.to_numeric(df['total_cases'].str.replace(',', ''), errors='coerce')
        df['new_cases'] = pd.to_numeric(df['new_cases'].str.replace('+', '').replace(',', ''), errors='coerce')
        df['total_deaths'] = pd.to_numeric(df['total_deaths'].str.replace(',', ''), errors='coerce')
        df['new_deaths'] = pd.to_numeric(df['new_deaths'].str.replace('+', '').replace(',', ''), errors='coerce')
        df['total_recovered'] = pd.to_numeric(df['total_recovered'].str.replace(',', ''), errors='coerce')
        df['active_cases'] = pd.to_numeric(df['active_cases'].str.replace(',', ''), errors='coerce')
        df['serious_critical'] = pd.to_numeric(df['serious_critical'].str.replace(',', ''), errors='coerce')
        df['total_cases_per_million'] = pd.to_numeric(df['total_cases_per_million'], errors='coerce')
        df['total_deaths_per_million'] = pd.to_numeric(df['total_deaths_per_million'], errors='coerce')
        df['total_tests'] = pd.to_numeric(df['total_tests'].str.replace(',', ''), errors='coerce')
        df['tests_per_million'] = pd.to_numeric(df['tests_per_million'], errors='coerce')
        df['population'] = pd.to_numeric(df['population'].str.replace(',', ''), errors='coerce')

            # Drop rows where 'total_cases' is NaN (or you can use another key column)
        df.dropna(subset=['total_cases'], inplace=True)

        df.fillna(0, inplace=True)  # Fill any remaining NaNs with 0
        
        return df

    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise
