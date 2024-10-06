import logging
from etl.extract import extract
from etl.transform import transform
from etl.load import load

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    """
    Orchestrates the entire ETL pipeline process.
    """
    try:
        logging.info("Pipeline started...")
        
        # Extract data
        extracted_data = extract()
        
        # Transform data
        transformed_data = transform(extracted_data)
        
        # Load data into the database
        load(transformed_data)
        
        logging.info("Pipeline completed successfully.")
    
    except Exception as e:
        logging.error(f"Pipeline encountered an error: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()
