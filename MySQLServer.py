import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Attempt to connect to MySQL Server
        connection = mysql.connector.connect(
            host="localhost",  
            user="root", 
            password="@Romanojuma3403"  
        )

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # Close the cursor and commit (commit is optional for database creation)
            cursor.close()

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handling any MySQL-related errors
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Ensure the connection is closed properly
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
