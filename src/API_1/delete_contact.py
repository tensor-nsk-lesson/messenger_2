from flask import Flask, request
import psycopg2

app = Flask(__name__)
# Создание контакта
@app.route("/contacts", methonds=['PUT'])
def login():
    connect = psycopg2.connect("host=90.189.168.29 dbname=messenger_2 user=messenger_2 password=messenger_2")
    cursor = connect.cursor()
    cursor.execute("SET search_path TO public")
    id_cont = request.form['user_id_cont']
    cursor.execute("UPDATE \"Contact\" SET 'cont_status' = '0' WHERE 'id_cont' = " + id_cont + ";")
    cursor.close()
    connect.commit()
    connect.close()

if __name__ == "__main__":
    app.run()
