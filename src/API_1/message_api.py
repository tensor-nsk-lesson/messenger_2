from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/login")
def index():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor =connect.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SELECT * FROM \"User\"")
    mes = ""
    for table in cursor.fetchall():
        mes += table.__str__() + "<br>"
        cursor.close()
        connect.close()
        return mes

if __name__ == "__main__":
    app.run()
