from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Получение одного сообщения
@app.route("/chat", methonds=['GET'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    mes_id = request.form['mes_id']
    cursor.execute("SELECT * FOR \"Message\" WHERE 'id_message' = " + mes_id + ";")
    mes = ''
    for table in cursor.fetchone():
        mes = table.__str__() + "<br>"
    cursor.close()
    connect.commit()
    connect.close()
    return mes

if __name__ == "__main__":
    app.run()
