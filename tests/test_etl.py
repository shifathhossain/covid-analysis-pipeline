import pandas as pd
from etl.transform import transform

def test_transform():
    """
    Tests the transform function with sample data.
    """
    sample_data = [
        {
            'country': 'CountryA',
            'total_cases': '1,000',
            'new_cases': '50',
            'total_deaths': '25',
            'new_deaths': '5',
            'total_recovered': '900',
            'active_cases': '75',
            'serious_critical': '10',
            'total_cases_per_million': '5000',
            'total_deaths_per_million': '250',
            'total_tests': '15,000',
            'tests_per_million': '750',
            'population': '2,000,000'
        },
        {
            'country': 'CountryB',
            'total_cases': '2,000',
            'new_cases': '+100',
            'total_deaths': '50',
            'new_deaths': '+10',
            'total_recovered': '1,800',
            'active_cases': '150',
            'serious_critical': '20',
            'total_cases_per_million': '10000',
            'total_deaths_per_million': '500',
            'total_tests': '30,000',
            'tests_per_million': '1500',
            'population': '3,000,000'
        },
        {
            'country': 'CountryC',
            'total_cases': '',
            'new_cases': '',
            'total_deaths': '',
            'new_deaths': '',
            'total_recovered': '',
            'active_cases': '',
            'serious_critical': '',
            'total_cases_per_million': '',
            'total_deaths_per_million': '',
            'total_tests': '',
            'tests_per_million': '',
            'population': ''
        }
    ]
    transformed_df = transform(sample_data)
    
    assert isinstance(transformed_df, pd.DataFrame)
    assert len(transformed_df) == 2  # CountryC should be dropped due to missing data
    assert transformed_df.iloc[0]['country'] == 'CountryA'
    assert transformed_df.iloc[0]['total_cases'] == 1000
    assert transformed_df.iloc[0]['new_cases'] == 50
    assert transformed_df.iloc[1]['country'] == 'CountryB'
    assert transformed_df.iloc[1]['total_cases'] == 2000
    assert transformed_df.iloc[1]['new_cases'] == 100
