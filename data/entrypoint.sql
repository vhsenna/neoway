CREATE SCHEMA IF NOT EXISTS neoway;

CREATE TABLE IF NOT EXISTS neoway.customers (
    id                        SERIAL PRIMARY KEY,
    cpf                       VARCHAR(20),
    private                   BOOLEAN,
    incomplete                BOOLEAN,
    last_order_date           DATE,
    average_ticket            DECIMAL(10,2),
    last_order_ticket         DECIMAL(10,2),
    most_frequent_store       VARCHAR(20),
    last_order_store          VARCHAR(20),
    valid_cpf                 BOOLEAN,
    valid_most_frequent_store BOOLEAN,
    valid_last_order_store    BOOLEAN,
    created_at                TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    validated_at              TIMESTAMP
);
