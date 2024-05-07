import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection parameters
dbname = "sensor_data"
user = "postgres"
password = "Adekunle_5880"
host = "localhost"  # or your PostgreSQL host address
port = "5432"  # default PostgreSQL port

# CSV file paths
trajectories = "/Users/expert/Desktop/10-Academy/week-2/sensor-data-project/utils/trajectories.csv"
vehicle = "/Users/expert/Desktop/10-Academy/week-2/sensor-data-project/utils/vehicle.csv"


def send_to_postgres():
# Connect to PostgreSQL
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cur = conn.cursor()

# Create SQLAlchemy engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Read CSV files into Pandas DataFrames
    trajectories_df = pd.read_csv(trajectories)
    vehicle_df = pd.read_csv(vehicle)

# Write DataFrames to PostgreSQL tables
    trajectories_df.to_sql('trajectories', engine, if_exists='replace', index=False)
    vehicle_df.to_sql('vehicle', engine, if_exists='replace', index=False)

# Commit and close connections
    conn.commit()
    conn.close()

    print("Data has been successfully loaded into PostgreSQL tables.")
