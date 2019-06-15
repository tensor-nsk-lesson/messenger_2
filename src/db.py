import psycopg2

def connect():
    connection = psycopg2.connect(
        database="messenger_2",
        user="messenger_2",
        password="messenger_2",
        host="90.189.168.29",
        port="5432"
    )
    return connection