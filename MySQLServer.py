import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",  # Change this if your MySQL server is on another host
            user="root",  # Replace with your MySQL username
            password="@Romanojuma3403"  # Replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Commit and close cursor
            connection.commit()
            cursor.close()

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close the connection to the MySQL server
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
