from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Удаление сообщения
@app.route("/chat", methonds=['PUT'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    id_mess = request.form['id_mess']
    cursor.execute("UPDATE \"Contact\" SET 'del_mes' = '1' WHERE 'id_message' = " + id_mess + ";")
    cursor.close()
    connect.commit()
    connect.close()

if __name__ == "__main__":
    app.run()
