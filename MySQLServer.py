import mysql.connector

try:
    # Connect to MySQL Server (not to a specific database yet)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"  # Replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database safely if it doesn't already exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    # Handle connection or SQL errors gracefully
    print("Error while connecting to MySQL:", e)

finally:
    # Always close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
