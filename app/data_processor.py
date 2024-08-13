import csv
import unicodedata
from datetime import datetime

from validators import validate_cnpj, validate_cpf


class DataProcessor:
    def __init__(self, db):
        self.db = db

    def process_file(self, file_path):
        with open(file_path, "r") as file:
            if file_path.endswith(".csv"):
                reader = csv.reader(file)
            else:
                reader = csv.reader(file, delimiter=" ", skipinitialspace=True)

            next(reader)

            data = []
            for row in reader:
                processed_row = self.process_row(row)
                data.append(processed_row)

            self.db.insert_data(data)

    def process_row(self, row):
        cpf = self.sanitize(row[0])[:20]
        private = bool(int(row[1]))
        incomplete = bool(int(row[2]))
        last_order_date = self.parse_date(row[3])
        average_ticket = self.parse_float(row[4])
        last_order_ticket = self.parse_float(row[5])
        most_frequent_store = self.sanitize(row[6])[:20]
        last_order_store = self.sanitize(row[7])[:20]

        valid_cpf = validate_cpf(cpf)
        valid_most_frequent_store = validate_cnpj(most_frequent_store)
        valid_last_order_store = validate_cnpj(last_order_store)
        validated_at = datetime.now()

        return (
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
        )

    @staticmethod
    def sanitize(text):
        return "".join(c for c in unicodedata.normalize("NFD", text)
                       if unicodedata.category(c) != "Mn").upper()

    @staticmethod
    def parse_date(date_str):
        return None if date_str == "NULL" else datetime.strptime(date_str, "%Y-%m-%d").date()

    @staticmethod
    def parse_float(value):
        return None if value == "NULL" else float(value.replace(".", "").replace(",", "."))
