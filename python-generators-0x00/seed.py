import mysql.connector
import csv

def connect_db():
    return mysql.connector.connect(
        host="airbnb",
        user="airbnb",
        password="StrongPass123"
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="airbnb",
        user="airbnb",
        password="StrongPass123",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS user_data (
                                                            user_id VARCHAR(36) NOT NULL PRIMARY KEY,
                       name VARCHAR(255) NOT NULL,
                       email VARCHAR(255) NOT NULL,
                       age DECIMAL NOT NULL,
                       INDEX(user_id)
                       )
                   """)
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    cursor.execute("SELECT user_id FROM user_data")
    existing = {row[0] for row in cursor.fetchall()}

    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        insert_rows = []
        for row in reader:
            if row['user_id'] not in existing:
                insert_rows.append((row['user_id'], row['name'], row['email'], row['age']))
        if insert_rows:
            cursor.executemany(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                insert_rows
            )
    connection.commit()
    cursor.close()
