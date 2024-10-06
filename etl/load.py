from sqlalchemy import create_engine
import yaml

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

def load(df):
    """
    Loads transformed data into the specified database.
    
    Args:
        df (pd.DataFrame): Transformed COVID-19 statistics.
    """
    config = load_config()
    db_type = config['database']['type']
    db_location = config['database']['location']
    
    if db_type == 'sqlite':
        engine = create_engine(f'sqlite:///{db_location}')
    else:
        raise ValueError("Unsupported database type")
    
    # Load data into 'coronavirus_stats' table
    df.to_sql('coronavirus_stats', engine, if_exists='append', index=False)
