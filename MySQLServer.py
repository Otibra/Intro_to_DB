# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

host = "localhost"
user = "root"
password = "password"
db_name = "alx_book_store"

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"Database '{db_name}' is ready.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password")
    else:
        print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()
