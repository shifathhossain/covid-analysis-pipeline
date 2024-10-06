from sqlalchemy import create_engine
import yaml
import logging

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

def load(df):
    """
    Loads transformed data into the specified database.
    
    Args:
        df (pd.DataFrame): Transformed COVID-19 statistics.
    """
    config = load_config()
    db_type = config['database']['type']
    db_location = config['database']['location']

    try:
        if db_type == 'sqlite':
            engine = create_engine(f'sqlite:///{db_location}')
            logging.info(f"Loading data into database: {db_location}")
        else:
            raise ValueError("Unsupported database type")

        # Load data into 'coronavirus_stats' table
        df.to_sql('coronavirus_stats', engine, if_exists='append', index=False)
        logging.info("Data successfully loaded into the database.")
    except Exception as e:
        logging.error(f"Error loading data into the database: {e}")
        raise
