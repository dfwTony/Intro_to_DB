import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (not to a database yet)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tony@#254"  # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Ensure the connection is properly closed
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
