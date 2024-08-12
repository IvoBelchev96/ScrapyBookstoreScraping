import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3307,
            user='root',
            password='Ivoivo16.',  # Replace with your password
            database='mysql'  # Default database to connect
        )
        if connection.is_connected():
            print("Successfully connected to MySQL")
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            for db in databases:
                print(db)
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    test_connection()
