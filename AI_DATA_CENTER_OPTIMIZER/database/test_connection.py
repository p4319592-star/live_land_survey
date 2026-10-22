from db import connect_database


try:
    connection = connect_database()
    print("SUCCESS: Python connected to PostgreSQL!")

    connection.close()

except Exception as error:
    print("CONNECTION FAILED:")
    print(error)