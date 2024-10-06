import pandas as pd

def transform(data):
    """
    Transforms raw scraped data into a structured DataFrame.
    
    Args:
        data (list of dict): Raw COVID-19 statistics.
    
    Returns:
        pd.DataFrame: Transformed data.
    """
    df = pd.DataFrame(data)
    
    # Data Cleaning
    df['country'] = df['country'].replace({'': None, 'Total:': 'World'})
    numeric_columns = [
        'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
        'total_recovered', 'active_cases', 'serious_critical',
        'total_cases_per_million', 'total_deaths_per_million',
        'total_tests', 'tests_per_million', 'population'
    ]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Remove entries without a country name
    df = df.dropna(subset=['country'])
    
    # Optional: Filter out aggregates like 'World'
    df = df[df['country'] != 'World']
    
    return df
