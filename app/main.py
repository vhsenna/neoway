import os
import time

import psycopg2
from data_processor import DataProcessor
from database import Database


def test_db_connection(db_url):
    try:
        conn = psycopg2.connect(db_url)
        print("Successfully connected to the database.")
        conn.close()
    except psycopg2.Error as e:
        print(f"Could not connect to the database. Error: {e}")
        exit(1)


def main():
    start_time = time.time()

    input_file = os.environ.get("INPUT_FILE", os.path.join("data", "base_test.txt"))
    db_url = os.environ.get("DATABASE_URL", "postgresql://admin:12345@db:5432/neoway")

    if not input_file:
        raise ValueError("The INPUT_FILE environment variable is not set.")
    if not db_url:
        raise ValueError("The DATABASE_URL environment variable is not set.")

    test_db_connection(db_url)

    db = Database(db_url)
    db.reset_table()
    processor = DataProcessor(db)

    processor.process_file(input_file)

    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()
