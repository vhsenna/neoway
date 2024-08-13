# Neoway Challenge

This project is a service designed to process and validate data from CSV or text files and store the results in a database. The project features a data processor that performs various validations and transformations, ensuring data quality before persisting it. The system leverages a database to maintain data integrity and provide reliable storage.

## Project Structure

```bash
neoway-challenge/
│
├── app/
│   ├── __init__.py
│   ├── data_processor.py          # Contains the DataProcessor class responsible for processing and validating data
│   ├── database.py                # Handles database operations and connections
│   ├── main.py                    # Entry point for the application, configures and starts the service
│   └── validators.py              # Contains validation functions for data fields (e.g., CPF, CNPJ)
│
├── data/
│   └── base_test.txt              # Sample database file for testing purposes
│
├── tests/
│   ├── test_data_processor.py
│   ├── test_database.py
│   ├── test_main.py
│   └── test_validators.py
│
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## Requirements

- Docker
- Docker Compose

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vhsenna/neoway-challenge.git
   cd neoway-challenge
   ```

2. Run the project with Docker Compose:

   ```bash
   docker compose up --build
   ```

This command will build the Docker image (if not already built) and start the necessary containers. The service will process the input file and insert the data into the PostgreSQL database.

## Testing

1. **Run the tests:**

   ```bash
   pytest
   ```

## Implementation Notes

- **CPF and CNPJ Validation:** The CPF and CNPJ validation in this project is fairly simplified. While this may be adequate for a prototype, it should be enhanced for production use. Ideally, use a dedicated library for these validations (such as [validate-docbr](https://pypi.org/project/validate-docbr/)) or government APIs for [CPF](https://www.gov.br/conecta/catalogo/apis/cadastro-base-do-cidadao-cbc-cpf) and [CNPJ](https://www.gov.br/conecta/catalogo/apis/consulta-cnpj).
- **Bulk Insertion (Future Enhancement):** Implementing a new function in `database.py` file for bulk insertion could significantly improve performance. Depending on the data volume, this method may be more efficient than the current line-by-line insertion loop. This enhancement should be considered if data volume increases or if performance issues become noticeable.
