# python-generators-0x00

## Project: Python Generators for Efficient Database Streaming

This project demonstrates advanced use of Python generators to handle large datasets efficiently, working with MySQL and the `user_data` table seeded from a CSV file.

### Setup

- MySQL Database Host: airbnb
- MySQL User: airbnb
- Password: StrongPass123
- Database: ALX_prodev
- Table: user_data (user_id [PK], name, email, age)

---

## Files

### seed.py

- **Purpose:** Initializes database and table, loads users from CSV.
- **Functions:**
    - `connect_db()`: Connects to MySQL server (no DB).
    - `create_database(connection)`: Creates ALX_prodev database.
    - `connect_to_prodev()`: Connects to ALX_prodev database.
    - `create_table(connection)`: Creates user_data table.
    - `insert_data(connection, csv_file)`: Inserts users from CSV.

---

### 0-stream_users.py

- **Purpose:** Streams user records one by one with a generator.
- **Function:**
    - `stream_users()`: Yields a dictionary per user row.

---

### 1-batch_processing.py

- **Purpose:** Batch-fetches users and filters by age > 25 efficiently.
- **Functions:**
    - `stream_users_in_batches(batch_size)`: Yields batches of N users.
    - `batch_processing(batch_size)`: Prints users > 25 using batches.

---

### 2-lazy_paginate.py

- **Purpose:** Implements lazy, page-by-page loading of users.
- **Functions:**
    - `paginate_users(page_size, offset)`: Fetches page from offset.
    - `lazy_pagination(page_size)`: Generator yields each page.

---

### 4-stream_ages.py

- **Purpose:** Streams user ages and computes the average without loading all data in memory.
- **Functions:**
    - `stream_user_ages()`: Yields ages.
    - `calculate_average_age()`: Calculates and prints average age.

---

## Usage

1. Run `seed.py` to set up and seed the database.
2. For each challenge, use the provided main scripts (`0-main.py`, `1-main.py`, etc.) to test generator functionality.
3. Ensure MySQL server is running with the correct host, user, password, and DB.
4. Manual QA and submission handled via GitHub (repo: `alx-backend-python`).

---

## Requirements

- Python 3.x
- mysql-connector-python
- MySQL database access as above
- CSV seed file: `user_data.csv`
- GitHub repo: `alx-backend-python` (directory `python-generators-0x00`)

