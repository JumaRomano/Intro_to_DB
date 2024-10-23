import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Change if your MySQL server is hosted elsewhere
            user='root',  # Replace with your MySQL username
            password='@Romanojuma3403'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection if they exist
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()