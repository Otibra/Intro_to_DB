-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS alx_book_store;

-- USE DATABASE
USE alx_book_store;

-- CREATE AUTHORS TABLE
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(255)
);

-- CREATE BOOKS TABLE
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- CREATE CUSTOMERS TABLE
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
);

-- CREATE ORDERS TABLE
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- CREATE ORDER DETAILS TABLE
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
