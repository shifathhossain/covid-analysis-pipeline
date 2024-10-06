from etl.extract import extract
from etl.transform import transform
from etl.load import load
from src.utils import setup_logging
import logging

def run_pipeline():
    """
    Runs the ETL pipeline: Extract, Transform, Load.
    """
    setup_logging()
    logging.info("Starting ETL pipeline...")
    try:
        # Extract
        data = extract()
        logging.info(f"Extracted {len(data)} records.")

        # Transform
        df = transform(data)
        logging.info(f"Transformed data into DataFrame with {len(df)} records.")

        # Load
        load(df)
        logging.info("Data loaded successfully into the database.")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
