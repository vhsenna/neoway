import psycopg2
from psycopg2.extras import execute_values


class Database:
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)
        self.create_schema()
        self.create_table()

    def create_schema(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE SCHEMA IF NOT EXISTS neoway;
            """)
        self.conn.commit()

    def create_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS neoway.customers (
                    id SERIAL PRIMARY KEY,
                    cpf VARCHAR(20),
                    private BOOLEAN,
                    incomplete BOOLEAN,
                    last_order_date DATE,
                    average_ticket NUMERIC(10,2),
                    last_order_ticket NUMERIC(10,2),
                    most_frequent_store VARCHAR(20),
                    last_order_store VARCHAR(20),
                    valid_cpf BOOLEAN,
                    valid_most_frequent_store BOOLEAN,
                    valid_last_order_store BOOLEAN,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    validated_at TIMESTAMP
                )
            """)
        self.conn.commit()

    def insert_data(self, data):
        with self.conn.cursor() as cur:
            execute_values(cur, """
                INSERT INTO neoway.customers (
                    cpf,
                    private,
                    incomplete,
                    last_order_date,
                    average_ticket,
                    last_order_ticket,
                    most_frequent_store,
                    last_order_store,
                    valid_cpf,
                    valid_most_frequent_store,
                    valid_last_order_store,
                    validated_at
                ) VALUES %s
            """, data)
        self.conn.commit()
        print(f"Inserted {len(data)} rows into the database.")

    def reset_table(self):
        with self.conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS neoway")
        self.conn.commit()
        self.create_table()
