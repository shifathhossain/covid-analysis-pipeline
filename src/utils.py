import logging
import os

def setup_logging():
    """
    Sets up logging for the pipeline.
    """
    os.makedirs('logs', exist_ok=True)
    logging.basicConfig(
        filename='logs/pipeline.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
