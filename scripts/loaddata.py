import pandas as pd
from sqlalchemy import create_engine

def load_data_to_rds(csv_path, user, password, host, port, database, table_name):
    try:
        df = pd.read_csv(csv_path, encoding='ISO-8859-1')
        print(f"Data loaded from {csv_path}")

        # connection string
        connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
        engine = create_engine(connection_string)

        with engine.connect() as connection:
            print("Connected to the database!")

            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Data loaded into table '{table_name}'")

            # query the table to verify data was inserted correctly
            query = f"SELECT * FROM {table_name};"
            df_result = pd.read_sql(query, connection)
            print("Data from the table:")
            print(df_result)

    except Exception as e:
        print(f"Error: {e}")