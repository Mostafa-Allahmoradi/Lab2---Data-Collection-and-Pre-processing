import psycopg2
from psycopg2 import sql
import pandas as pd

def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "DOUBLE PRECISION"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "TIMESTAMP"
    else:
        return "VARCHAR(50)"

class DBManager:

    def __init__(self, data):
        """Neon requires that all connections use SSL/TLS encryption to ensure data security and prevent unauthorized access or manipulation during transmission."""
        self.db_config = {
            "host": "ep-summer-fog-adiafnk0-pooler.c-2.us-east-1.aws.neon.tech",
            "database": "neondb",
            "user": "neondb_owner",
            "password": "npg_ZvBa8w1tNjnQ",
            "port": "5432",
            "sslmode": "require",
        }
        self.table_name = "Shipping_Addresses"
        self.data = data
        self.connection = self._connect()

    def _connect(self):
        """Establish a connection to the PostgreSQL database."""
        return psycopg2.connect(**self.db_config)
    
    # Creates a table in the database (if it doesn’t already exist).
    def _drop_and_create_table(self):
        """Drop and recreate the table from scratch."""
        drop_query = f"DROP TABLE IF EXISTS \"{self.table_name}\";"

        column_defs = [(col, map_dtype(dtype)) for col, dtype in self.data.dtypes.items() ]
        create_query = sql.SQL("CREATE TABLE IF NOT EXISTS {table} ({fields})").format(
                    table=sql.Identifier(self.table_name),
                    fields=sql.SQL(", ").join(
                        sql.SQL("{} {}").format(sql.Identifier(col), sql.SQL(dtype))
                        for col, dtype in column_defs
                    ))
        
        with self.connection as conn:
            with conn.cursor() as cur:
                cur.execute(drop_query)
                cur.execute(create_query)
                conn.commit()
        print(f"🔁 {self.table_name} table dropped and recreated.")

    def _insert_into_table(self):
        cols = ', '.join(f'"{c}"' for c in self.data.columns)        # quote column names safely
        placeholders = ', '.join(['%s'] * len(self.data.columns))    # build %s placeholders
        insert_query = f'INSERT INTO "{self.table_name}" ({cols}) VALUES ({placeholders})'
        with self.connection as conn:
            with conn.cursor() as cur:
                for row in self.data.itertuples(index=False, name=None):
                    cur.execute(insert_query, row)
                conn.commit()
        print(f"{len(self.data)} rows inserted!")

    def _fect_all(self):
        # print("🔍 Fetching all records from the database...")
        sql_query = f"SELECT * FROM \"{self.table_name}\";"

        # Fetches all records from the database.
        with self.connection as conn:
            df = pd.read_sql_query(sql_query, conn) 
            print(f"✅ Successfully loaded {len(df)} rows from {self.table_name} table.")
        return df