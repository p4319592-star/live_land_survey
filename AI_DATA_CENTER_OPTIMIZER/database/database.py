import psycopg2


def connect_database():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="data_center",
        user="postgres",
        password="HERO"
    )