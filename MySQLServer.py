# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

# MySQL server credentials
host = "localhost"      # Change if your server is remote
user = "root"           # Your MySQL username
password = "password"   # Your MySQL password

# Database name
db_name = "alx_book_store"

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    # Attempt to create the database
    cursor.execute(f"CREATE DATABASE {db_name}")
    print(f"Database '{db_name}' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_DB_CREATE_EXISTS:
        # Database already exists; do not fail
        print(f"Database '{db_name}' already exists.")
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist")
    else:
        print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
