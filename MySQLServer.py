import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',         # Replace with your host, e.g., 'localhost' or IP address
            user='root',     # Replace with your MySQL username
            password='is711ib2012'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
