import pandas as pd
from sqlalchemy import create_engine

def verify_data():
    engine = create_engine('sqlite:///data/processed/data.db')
    df = pd.read_sql('SELECT * FROM coronavirus_stats', engine)
    print(df.head())

verify_data()